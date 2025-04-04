# run_all.sh
#!/bin/bash

set -e

echo "[1] Installation des dépendances"
pip install -r requirements.txt

echo "[2] Démonstration pipeline général"
python examples/example_pipeline.py

echo "[3] Démonstration multimodale"
python examples/example_multimodal.py

echo "[4] Export ONNX"
python tools/export_onnx.py

echo "[5] Benchmark"
python tools/benchmark.py