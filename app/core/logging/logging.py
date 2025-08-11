import sys
from loguru import logger
from pathlib import Path
from app.core.config import settings

# Create logs directory if it doesn't exist
log_path = Path("logs")
log_path.mkdir(exist_ok=True)

# Configure loguru
logger.remove()  # Remove default handler

# Add console handler
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level=settings.LOG_LEVEL,
    serialize=settings.LOG_FORMAT == "json",
)

# Add file handler
logger.add(
    settings.LOG_FILE,
    rotation=settings.LOG_ROTATION,
    retention=settings.LOG_RETENTION,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level=settings.LOG_LEVEL,
    serialize=settings.LOG_FORMAT == "json",
    diagnose=True,
    backtrace=True
) 