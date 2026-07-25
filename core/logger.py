from pathlib import Path
from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    LOG_DIR / "tbh.log",
    rotation="5 MB",
    retention=10,
    level="INFO"
)

logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO"
)