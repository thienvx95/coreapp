from app.core.constants import Application_Version
from app.core.data.base_db import BaseDatabase
from app.core.data.mongo_db.mongo_repository import BaseRepository
from app.entities.application import ApplicationInfo


class ApplicationInfoService:
    application_info: ApplicationInfo = None
    def __init__(self, db: BaseDatabase):
        repository = BaseRepository(db, "application_info", ApplicationInfo)
        super().__init__(repository)
        self.repository = repository
        self.db = db

    async def get_application_info(self):
        if self.application_info == None:
            self.application_info = await self.repository.find_one()
        return self.application_info

    async def set_application_info(self):
        new_model = ApplicationInfo()
        new_model.app_version = Application_Version
        new_model.database_version = self.db.client.get_database().name
