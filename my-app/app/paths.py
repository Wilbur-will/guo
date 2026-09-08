from pathlib import Path

APP_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_DATA_DIR = APP_ROOT / 'data' / 'runtime'
RUNTIME_DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = RUNTIME_DATA_DIR / 'users.db'
