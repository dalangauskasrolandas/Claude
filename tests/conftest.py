import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ["EXPIRYWATCH_DB"] = os.path.join(tempfile.mkdtemp(), "test.db")

import pytest  # noqa: E402


@pytest.fixture(scope="session", autouse=True)
def samples():
    subprocess.run([sys.executable, os.path.join(ROOT, "make_samples.py")], check=True)


@pytest.fixture(autouse=True)
def clean_db():
    import app
    if os.path.exists(app.DB_PATH):
        os.remove(app.DB_PATH)
    yield
