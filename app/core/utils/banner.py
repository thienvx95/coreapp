from app.core.logging import logger
from app.core.config import settings

def get_banner():
    logger.info("=" * 50)
    logger.info(f"    App name          : {settings.APP_NAME}")
    logger.info(f"    App version       : {settings.APP_VERSION}")
    logger.info(f"    Environment       : {settings.APP_ENV}")
    logger.info(f"    Debug mode        : {settings.DEBUG}")
    logger.info(f"   Database Provider : {settings.DB_PROVIDER}")
    logger.info(f"   Database Version  : {settings.DEBUG}")
    logger.info(f"   Database Name     : {settings.DATABASE_NAME}")
    logger.info(f"   Storage Provider  : {settings.DEBUG}")
    logger.info(f"   Cache Provider    : {settings.CACHE_PROVIDER}")
    logger.info(f"   Log Level         : {settings.LOG_LEVEL}")
    logger.info(f"   API URL           : http://{settings.HOST}:{settings.PORT}{settings.API_V1_STR}")
    logger.info(f"   Swagger URL       : http://{settings.HOST}:{settings.PORT}{settings.SWAGGER_URL}")
    logger.info("=" * 50)
