import json
from typing import List

from app.business.menu.entities.menu import Menu
from app.business.roles.entities.role import Role
from app.business.seed.view_model.model_seed import ModelSeed
from app.business.setting.entities.setting import Setting
from app.business.user.entities.user import User
from app.core.logging import logger 
from app.core.data.repository_factory import RepositoryFactory
from app.business.common.services.file_reader.file_reader_service import FileReaderService

class MongoSeeder:
    models: List[ModelSeed] = [
        ModelSeed(User, "./seed/1.users/user.json"),
        ModelSeed(Role, "./seed/2.roles/role.json"),
        ModelSeed(Menu, "./seed/3.menus/menus.json"),
        ModelSeed(Setting, "./seed/4.settings/setting.json"),
    ]

    def __init__(self, file_reader_service: FileReaderService):
        self.file_reader_service = file_reader_service

    async def seed(self) -> bool:
        try:
            for seed in self.models:
                content = self.file_reader_service.read_file(seed.path)
                object_data = json.loads(content)
                print(content)  
            
                repo = RepositoryFactory().get_repository(model=seed.model)
                await repo.insert_many(object_data)
            return True
        except Exception as e:
            logger.error(e)
            return False
