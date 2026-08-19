#!/bin/bash
set -e

PYTHON_BIN="${PYTHON_BIN:-python3}"

echo "[1/5] Checking Python..."
$PYTHON_BIN --version

echo "[2/5] Creating virtual environment..."
$PYTHON_BIN -m venv .venv
source .venv/bin/activate

echo "[3/5] Installing all dependencies from requirements.txt..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "[4/5] Building the knowledge base..."
python scripts/ingest.py

echo "[5/5] Running tests..."
PYTHONPATH=. python -m pytest -q

echo
 echo "Setup complete. Start the app with:"
echo "source .venv/bin/activate && python -m uvicorn app.main:app --reload"
echo "Then open http://127.0.0.1:8000"
