from app.core.logging import logger
from app.core.config import settings
from app.core.constants import Application_Version
from app.core.data import DBFactory
from app.business.application_info.entities.application_info import ApplicationInfo
from app.business.common.entities.migration_db.migration_db import MigrationDB
from app.core.container import Container

class ApplicationInfoService:
    application_info: ApplicationInfo = None
    def __init__(self, repository_factory):
        self.repository = repository_factory(collection_name="application_info", model=ApplicationInfo)
        self.db_migration_repository = repository_factory(collection_name="migration_dbs", model=MigrationDB)

    async def get_application_info(self):
        """
        Retrieves application information, loading from cache, then repository,
        and setting a default if not found.
        """
        try:
            # 1. Check if info is already cached
            if self.application_info is not None:
                return self.application_info

            # 2. If not cached, try to load from the repository
            loaded_info: ApplicationInfo | None = await self.repository.find_one({})
            print(loaded_info)
            # 3. If loaded successfully, cache it
            if loaded_info is not None:
                self.application_info = loaded_info
            else:
                await self.set_application_info() # Call the method to set the default

            return self.application_info
        except Exception as e:
            logger.error(f"Failed to get application info in repository: {e}", exc_info=True)
            return None

    async def set_application_info(self, application_info: ApplicationInfo = None):
        try:
            application_info: ApplicationInfo | None = await self.repository.find_one({})
            migration_db: MigrationDB | None = await self.db_migration_repository.find_one({})
            db_provider = DBFactory().get_provider()
            db_version = await db_provider.get_database_version()
            db_name = await db_provider.get_database_name()
            
            if application_info is None:
                application_info = ApplicationInfo(
                    app_version=Application_Version,
                    database_name=db_name,
                    database_version=db_version,
                    database_provider=settings.DB_PROVIDER,
                    cache_provider=settings.CACHE_PROVIDER,
                    database_migration=getattr(migration_db, "id", "")
                )
                await self.repository.insert_one(application_info)
            else:
                application_info.app_version=Application_Version
                application_info.database_name=db_name
                application_info.database_version=db_version
                application_info.database_provider=settings.DB_PROVIDER
                application_info.cache_provider=settings.CACHE_PROVIDER
                application_info.database_migration=getattr(migration_db, "id", "")
                await self.repository.update_one({'id': application_info.id }, application_info)
     
            # Optionally update the cached info after creation
            self.application_info = application_info
        except Exception as e:
            logger.error(f"Failed to set application info in repository: {e}", exc_info=True)

    async def get_migration_db_info(self):
        try:
            self.db_migration_repository
        except Exception as e:
            logger.error(f"Failed to get migration db: {e}", exc_info=True)


