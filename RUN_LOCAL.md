# Run locally (macOS)

## Recommended one-time setup

From the project folder:

```bash
bash setup_mac.sh
```

This creates `.venv`, installs **all** packages from `requirements.txt`, rebuilds the knowledge base, and runs the test suite.

Expected result:

```text
10 passed
```

## Start the application

```bash
source .venv/bin/activate
python -m uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## Manual setup if you do not want the script

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/ingest.py
PYTHONPATH=. python -m pytest -q
python -m uvicorn app.main:app --reload
```

## Browser voice

Use Chrome or another browser that supports the Web Speech API and allow microphone access when prompted. If speech recognition is unavailable, use the text box; the same screening backend is used.

## Expected behavior tests

1. Cooperative candidate -> normal screening.
2. Objection -> grounded objection response.
3. Conflicting experience -> clarification before storing the answer.
4. Out-of-scope question -> safe fallback; it must not be stored as the current screening field.
5. Human request -> `HUMAN_ESCALATION`.
6. Salary question -> explicit grounded statement that salary is not in the KB, with source citation.
