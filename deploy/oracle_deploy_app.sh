#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 ubuntu@YOUR_SERVER_IP" >&2
  exit 1
fi

TARGET="$1"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KEY_PATH="$ROOT_DIR/oracle_guo_chuang_key"

rsync -az --delete \
  -e "ssh -i $KEY_PATH -o IdentitiesOnly=yes" \
  --exclude '.DS_Store' \
  --exclude '__pycache__' \
  --exclude '*.pyc' \
  --exclude 'data/runtime/*.db' \
  "$ROOT_DIR/my-app/" "$TARGET:/opt/guo_chuang/my-app/"

ssh -i "$KEY_PATH" -o IdentitiesOnly=yes "$TARGET" \
  "cd /opt/guo_chuang/my-app && /opt/guo_chuang/.venv/bin/python -m pip install -r requirements.txt && sudo systemctl restart guo-chuang && sudo systemctl status guo-chuang --no-pager"
