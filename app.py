"""ExpiryWatch - local expiry tracker for business documents.

Run:   python app.py            (web UI on http://localhost:5000)
Check: python app.py --check    (print documents expiring within 60 days)
"""
import csv
import io
import os
import sqlite3
import sys
from datetime import date, datetime

from flask import Flask, Response, jsonify, render_template_string, request

import extractor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.environ.get("EXPIRYWATCH_DB", os.path.join(BASE_DIR, "expirywatch.db"))
CHECK_DAYS = 60

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 200 * 1024 * 1024


# --------------------------------------------------------------------------- db

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("""CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        doc_type TEXT NOT NULL DEFAULT '',
        holder TEXT NOT NULL DEFAULT '',
        expiry TEXT,
        status TEXT NOT NULL DEFAULT 'review',   -- ok | review | scanned
        note TEXT NOT NULL DEFAULT '',
        uploaded_at TEXT NOT NULL)""")
    return conn


# --------------------------------------------------------------------------- rules

def days_left(expiry, today=None):
    if not expiry:
        return None
    return (date.fromisoformat(expiry) - (today or date.today())).days


def colour(status, expiry, today=None):
    d = days_left(expiry, today)
    if status != "ok" or d is None:
        return "grey"
    if d < 7:
        return "red"
    if d < 30:
        return "orange"
    if d < 60:
        return "yellow"
    return "green"


def as_dict(row, today=None):
    r = dict(row)
    r["days_left"] = days_left(r["expiry"], today)
    r["colour"] = colour(r["status"], r["expiry"], today)
    return r


def all_documents(today=None):
    with db() as conn:
        rows = conn.execute("SELECT * FROM documents").fetchall()
    docs = [as_dict(r, today) for r in rows]
    docs.sort(key=lambda r: (r["days_left"] is None, r["days_left"] or 0, r["filename"].lower()))
    return docs


def expiring_soon(days=CHECK_DAYS, today=None):
    return [d for d in all_documents(today) if d["days_left"] is not None and d["days_left"] < days]


# --------------------------------------------------------------------------- routes

@app.get("/")
def index():
    return render_template_string(PAGE)


@app.get("/api/documents")
def api_list():
    return jsonify(all_documents())


@app.post("/api/upload")
def api_upload():
    results = []
    for f in request.files.getlist("files"):
        name = os.path.basename(f.filename or "unnamed")
        if not name.lower().endswith(".pdf"):
            results.append({"filename": name, "error": "Not a PDF"})
            continue
        try:
            info = extractor.analyse(extractor.extract_text(io.BytesIO(f.read())))
        except Exception:
            info = dict(doc_type="", holder="", expiry=None, status="scanned",
                        note="Unreadable PDF, needs manual entry")
        with db() as conn:
            conn.execute(
                "INSERT INTO documents (filename, doc_type, holder, expiry, status, note, uploaded_at)"
                " VALUES (?,?,?,?,?,?,?)",
                (name, info["doc_type"], info["holder"], info["expiry"], info["status"],
                 info["note"], datetime.now().isoformat(timespec="seconds")))
        results.append({"filename": name, "status": info["status"]})
    return jsonify(results)


@app.post("/api/documents/<int:doc_id>")
def api_update(doc_id):
    data = request.get_json(force=True)
    expiry = (data.get("expiry") or "").strip() or None
    if expiry:
        try:
            date.fromisoformat(expiry)
        except ValueError:
            return jsonify(error="Expiry must be YYYY-MM-DD"), 400
    filename = (data.get("filename") or "").strip()
    if not filename:
        return jsonify(error="File name cannot be empty"), 400
    status, note = ("ok", "Edited manually") if expiry else ("review", "No expiry date")
    with db() as conn:
        cur = conn.execute(
            "UPDATE documents SET filename=?, doc_type=?, holder=?, expiry=?, status=?, note=?"
            " WHERE id=?",
            (filename, (data.get("doc_type") or "").strip(), (data.get("holder") or "").strip(),
             expiry, status, note, doc_id))
    if not cur.rowcount:
        return jsonify(error="Not found"), 404
    return jsonify(ok=True)


@app.delete("/api/documents/<int:doc_id>")
def api_delete(doc_id):
    with db() as conn:
        conn.execute("DELETE FROM documents WHERE id=?", (doc_id,))
    return jsonify(ok=True)


def _safe(value):
    """Neutralise spreadsheet formulas in text coming from PDFs."""
    value = "" if value is None else str(value)
    return "'" + value if value[:1] in ("=", "+", "-", "@", "\t", "\r") else value


def csv_text(today=None):
    out = io.StringIO()
    w = csv.writer(out, delimiter=";", lineterminator="\r\n")
    w.writerow(["File name", "Type", "Holder", "Expiry date", "Days left", "Status", "Note"])
    for d in all_documents(today):
        w.writerow([_safe(d["filename"]), _safe(d["doc_type"]), _safe(d["holder"]),
                    d["expiry"] or "", "" if d["days_left"] is None else d["days_left"],
                    {"ok": "OK", "review": "Needs review", "scanned": "Scanned, needs manual entry"}[d["status"]],
                    _safe(d["note"])])
    return out.getvalue()


@app.get("/export.csv")
def export_csv():
    # UTF-8 BOM + semicolon: opens correctly (accents, Cyrillic, columns) in Excel
    body = "﻿" + csv_text()
    return Response(body, mimetype="text/csv; charset=utf-8",
                    headers={"Content-Disposition": "attachment; filename=expirywatch.csv"})


# --------------------------------------------------------------------------- CLI

def run_check(today=None, days=CHECK_DAYS):
    docs = expiring_soon(days, today)
    if not docs:
        print(f"No documents expiring within {days} days.")
        return 0
    print(f"Documents expiring within {days} days ({len(docs)}):")
    for d in docs:
        left = d["days_left"]
        when = f"EXPIRED {-left} days ago" if left < 0 else f"{left} days left"
        flag = "" if d["status"] == "ok" else "  [needs review]"
        print(f"  {d['expiry']}  {when:<22} {d['doc_type'] or '-':<22} "
              f"{d['holder'] or '-':<30} {d['filename']}{flag}")
    return len(docs)


# --------------------------------------------------------------------------- page

PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>ExpiryWatch</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
 body{font-family:system-ui,sans-serif;margin:0;background:#f5f6f8;color:#1c2330}
 main{max-width:1100px;margin:0 auto;padding:24px 16px}
 h1{margin:0 0 16px;font-size:24px}
 #drop{border:2px dashed #8a94a6;border-radius:10px;padding:28px;text-align:center;background:#fff;cursor:pointer}
 #drop.over{border-color:#2563eb;background:#eef4ff}
 #msg{margin:10px 0;min-height:20px;font-size:14px}
 .bar{display:flex;justify-content:space-between;align-items:center;margin:16px 0 8px}
 table{width:100%;border-collapse:collapse;background:#fff}
 td:nth-child(4),td:nth-child(5){white-space:nowrap}
 th,td{padding:8px 10px;text-align:left;border-bottom:1px solid #e3e6ec;font-size:14px;vertical-align:middle}
 th{background:#eceff4}
 td input{width:100%;box-sizing:border-box;padding:4px}
 tr.red td{background:#fecaca} tr.orange td{background:#fed7aa}
 tr.yellow td{background:#fef08a} tr.green td{background:#bbf7d0} tr.grey td{background:#e5e7eb}
 button,a.btn{font:inherit;padding:4px 10px;border:1px solid #8a94a6;border-radius:6px;background:#fff;cursor:pointer;text-decoration:none;color:inherit}
 .note{color:#4b5563;font-size:12px}
 @media (max-width:700px){main{padding:12px}}
</style></head><body><main>
<h1>ExpiryWatch</h1>
<div id="drop">Drop PDFs here or click to choose<input id="file" type="file" accept=".pdf" multiple hidden></div>
<div id="msg" role="status"></div>
<div class="bar"><strong id="count"></strong><a class="btn" href="/export.csv">Export CSV</a></div>
<div style="overflow-x:auto"><table><thead><tr>
 <th>File name</th><th>Type</th><th>Holder / vehicle</th><th>Expiry date</th><th>Days left</th><th>Status</th><th></th>
</tr></thead><tbody id="rows"></tbody></table></div>
<script>
const $=s=>document.querySelector(s), msg=t=>$('#msg').textContent=t;
const LABEL={ok:'OK',review:'Needs review',scanned:'Scanned, needs manual entry'};
function td(text){const c=document.createElement('td');c.textContent=text;return c}
function btn(text,fn){const b=document.createElement('button');b.textContent=text;b.onclick=fn;return b}
async function load(){
  const docs=await (await fetch('/api/documents')).json();
  $('#count').textContent=docs.length+' document'+(docs.length==1?'':'s');
  const body=$('#rows');body.replaceChildren();
  for(const d of docs) body.append(row(d));
}
function row(d){
  const tr=document.createElement('tr');tr.className=d.colour;
  const left=d.days_left==null?'':(d.days_left<0?'expired '+(-d.days_left)+' d ago':d.days_left);
  const st=td(LABEL[d.status]);
  if(d.note&&d.status!=='ok'){const n=document.createElement('div');n.className='note';n.textContent=d.note;st.append(n)}
  const act=document.createElement('td');
  act.append(btn('Edit',()=>edit(tr,d)),' ',btn('Delete',async()=>{
    if(confirm('Delete '+d.filename+'?')){await fetch('/api/documents/'+d.id,{method:'DELETE'});load()}}));
  tr.append(td(d.filename),td(d.doc_type),td(d.holder),td(d.expiry||''),td(left),st,act);
  return tr;
}
function edit(tr,d){
  tr.replaceChildren();
  const inp=(v,t)=>{const i=document.createElement('input');i.type=t||'text';i.value=v||'';return i};
  const f=inp(d.filename),t=inp(d.doc_type),h=inp(d.holder),e=inp(d.expiry,'date');
  const cell=x=>{const c=document.createElement('td');c.append(x);return c};
  const act=document.createElement('td');
  act.append(btn('Save',async()=>{
    const r=await fetch('/api/documents/'+d.id,{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({filename:f.value,doc_type:t.value,holder:h.value,expiry:e.value})});
    if(r.ok){load()}else{msg((await r.json()).error)}}),' ',btn('Cancel',load));
  tr.append(cell(f),cell(t),cell(h),cell(e),td(''),td('Saving marks it OK'),act);
}
async function upload(files){
  const fd=new FormData();for(const f of files)fd.append('files',f);
  msg('Reading '+files.length+' file(s)...');
  const res=await (await fetch('/api/upload',{method:'POST',body:fd})).json();
  const bad=res.filter(r=>r.error), review=res.filter(r=>r.status&&r.status!=='ok');
  msg((res.length-bad.length)+' added, '+review.length+' need review'+(bad.length?', '+bad.length+' rejected (not PDF)':''));
  load();
}
const drop=$('#drop'),file=$('#file');
drop.onclick=()=>file.click();file.onchange=()=>{upload(file.files);file.value=''};
drop.ondragover=e=>{e.preventDefault();drop.classList.add('over')};
drop.ondragleave=()=>drop.classList.remove('over');
drop.ondrop=e=>{e.preventDefault();drop.classList.remove('over');upload(e.dataTransfer.files)};
load();
</script></main></body></html>"""


if __name__ == "__main__":
    if "--check" in sys.argv[1:]:
        run_check()
        sys.exit(0)
    print("ExpiryWatch running at http://localhost:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
