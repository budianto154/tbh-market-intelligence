from pathlib import Path

# Folder utama project
BASE_DIR = Path(__file__).resolve().parent

# Folder data
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Folder logs
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Database SQLite
DATABASE_URL = f"sqlite:///{DATA_DIR / 'market.db'}"

# Steam App ID TaskBar Heroes
STEAM_APP_ID = 3678970

# Konfigurasi scraper
HEADLESS = False
REQUEST_DELAY = 2