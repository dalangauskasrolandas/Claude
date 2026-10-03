#!/usr/bin/env python3
"""Heuristic lint for the research markdown files.
1) Flags lines that contain numbers but no evidence label ([V:..], [E:..], UNKNOWN).
2) Checks that every [V:id] exists in sources.csv and every [E:id] exists in assumptions.md.
3) Reports EE/LV/LT coverage per file.
Usage: python3 lint_labels.py [files...]  (default: research/0*.md, red_team.md, verification_log.md)
"""
import csv, glob, os, re, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

LABEL_RE = re.compile(r'\[(?:V|E):[^\]]+\]|UNKNOWN|VERIFIED|ESTIMATE|\[V\]|\[E\]')
STRIP_PATTERNS = [
    r'https?://\S+', r'\[(?:V|E):[^\]]+\]', r'`[^`]*`',
    r'\bA-WS\d-\d+\b', r'\bWS\d-\d+\b', r'\bWS\d\b', r'\bVL-\d+\b', r'\bRT-\d+\b',
    r'\b[a-z]{2,}(?:_[a-z0-9]+)+\b',                  # dataset codes like isoc_eb_ai
    r'\b[A-Z]{2,5}\d{2,4}[A-Z]?\b',                  # table ids like ER026, UZS010
    r'\b[A-U]\s?\d{2}(?:\.\d{1,2})?(?:\s?[–-]\s?[A-U]?\d{2}(?:\.\d{1,2})?)?\b',  # NACE
    r'\bNACE\s*(?:Rev\.?\s*)?\d(?:\.\d)?\b',
    r'\b\d{8}-\d\b',                                  # CPV
    r'\bISCO(?:-08)?\s*\d{1,4}\b',
    r'§+\s*\d+[¹²³⁴⁵⁶⁷⁸⁹⁰]*(?:\s*(?:lg|lõige|lõike|p|punkt|par\.?)\s*\d+)*',
    r'\b(?:Art(?:icle|\.)?|Arts\.|Section|Sec\.|Recital|Annex|Chapter|Regulation|Reg\.|Directive|Dir\.|Law No\.?|No\.)\s*\d+[a-z]?(?:\s*\(\d+\)(?:\s*\([a-z]\))?)*(?:/\d+)*(?:/(?:EU|EC|EEC))?',
    r'\(\d+\)(?:\([a-z]\))?',
    r'\b(?:C|T)-\d+/\d+\b',                           # CJEU case numbers
    r'\b\d{1,2}\.\d{1,2}\.\d{4}\b', r'\b\d{4}-\d{2}(?:-\d{2})?\b', r'\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{4}\b',
    r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}(?:,\s*\d{4})?\b',
    r'\b(?:19|20)\d{2}(?:[–/-](?:19|20)?\d{2})?s?\b',  # years and year ranges
    r'\bQ[1-4]\b', r'\bH[12]\b', r'\bG[12]\b', r'\bB2[BC]\b', r'\bn8n\b', r'\b365\b(?=\s|$)', r'\b[0-9]+G\b',
    r'\bEU-?2[78]\b', r'\bA\+B(?:\+C)?\b', r'\bS[1-9]\b', r'\bS(?:9|10)\b',
    r'^\s*\d+[.)]\s', r'^#+\s*[\d.]+\s', r'^\s*[-*]\s*\d+[.)]\s',
    r'\bISO\s?\d+\b', r'\b(?:GPT|Claude|Llama)[- ]?\d[\w.]*\b', r'\bWeb\d\b', r'\bv\d+(?:\.\d+)*\b',
    r'\b(?:Pillar|pillar)\s+(?:II|2)\b', r'\bII\b', r'\b1st|2nd|3rd|\d+th\b',
]
STRIP_RE = [re.compile(p, flags=re.I if i not in (6,7) else 0) for i, p in enumerate(STRIP_PATTERNS)]
DIGIT_RE = re.compile(r'\d')

def load_ids():
    src, asm = set(), set()
    p = os.path.join(ROOT, 'sources.csv')
    if os.path.exists(p):
        with open(p, newline='', encoding='utf-8') as fh:
            for r in csv.DictReader(fh): src.add(r['id'].strip())
    for f in glob.glob(os.path.join(ROOT, '_work', 'sources_*.csv')):
        with open(f, newline='', encoding='utf-8') as fh:
            for r in csv.DictReader(fh):
                if r.get('id'): src.add(r['id'].strip())
    texts = []
    p = os.path.join(ROOT, 'assumptions.md')
    if os.path.exists(p): texts.append(open(p, encoding='utf-8').read())
    for f in glob.glob(os.path.join(ROOT, '_work', 'assumptions_*.md')): texts.append(open(f, encoding='utf-8').read())
    for t in texts: asm.update(re.findall(r'^###\s+(A-WS\d-\d+)', t, flags=re.M))
    return src, asm

def lint(path, src, asm):
    unl, bad_v, bad_e = [], [], []
    in_code = False
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        s = line.rstrip('\n')
        if s.strip().startswith('```'): in_code = not in_code; continue
        if in_code or not s.strip(): continue
        for tag in re.findall(r'\[V:([^\]]+)\]', s):
            for i in re.split(r'[,;\s]+', tag.strip()):
                if i and re.match(r'WS\d-\d+|VL-\d+|RT-\d+', i) and i not in src: bad_v.append((n, i))
        for tag in re.findall(r'\[E:([^\]]+)\]', s):
            for i in re.split(r'[,;\s]+', tag.strip()):
                if i and re.match(r'A-WS\d-\d+', i) and i not in asm: bad_e.append((n, i))
        if LABEL_RE.search(s): continue
        t = s
        for rx in STRIP_RE: t = rx.sub(' ', t)
        if DIGIT_RE.search(t): unl.append((n, s.strip()[:160]))
    return unl, bad_v, bad_e

def coverage(path):
    txt = open(path, encoding='utf-8').read()
    c = {k: len(re.findall(p, txt)) for k, p in
         {'EE': r'\bEE\b|Estonia', 'LV': r'\bLV\b|Latvia', 'LT': r'\bLT\b|Lithuania'}.items()}
    return c

def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, '0*.md'))) + \
        [p for p in [os.path.join(ROOT, 'red_team.md'), os.path.join(ROOT, 'verification_log.md')] if os.path.exists(p)]
    src, asm = load_ids()
    print(f'known source ids: {len(src)} | assumption ids: {len(asm)}')
    for f in files:
        unl, bv, be = lint(f, src, asm)
        print(f'\n== {os.path.relpath(f, ROOT)} | coverage {coverage(f)} | unlabelled-number lines: {len(unl)} | missing V ids: {len(bv)} | missing E ids: {len(be)}')
        for n, s in unl[:400]: print(f'  L{n}: {s}')
        if bv: print('  missing V ids:', sorted({i for _, i in bv})[:60])
        if be: print('  missing E ids:', sorted({i for _, i in be})[:60])

if __name__ == '__main__':
    main()
