import json
from typing import List

from app.business.menu.schema import Menu
from app.business.account.schema.role import Role
from app.business.seed.model import ModelSeed
from app.business.setting.schema import Setting
from app.business.account.schema.user import User
from app.core.data.model_type import ModelType
from app.core.logging import logger 
from app.core.data.repository_factory import RepositoryFactory
from app.business.common.services.file_reader.file_reader_service import FileReaderService

class SeederService:
    account_models: List[ModelSeed] = [
        ModelSeed(Role, "./seed/2.roles/role.json"),
        ModelSeed(User, "./seed/1.users/user.json"),
    ]
    menu_models: List[ModelSeed] = [
        ModelSeed(Menu, "./seed/3.menus/menus.json"),
    ]
    setting_models: List[ModelSeed] = [
        ModelSeed(Setting, "./seed/4.settings/setting.json"),
    ]

    def __init__(self, file_reader_service: FileReaderService):
        self.file_reader_service = file_reader_service

    async def seed(self) -> bool:
        await self.run_seed_account()
        await self.run_seed(self.menu_models)
        await self.run_seed(self.setting_models)
        return True
        
    async def run_seed_account(self) -> bool:
        # Create role
        list_role_data = self.read_file("./seed/2.roles/role.json")
        repo = RepositoryFactory().get_repository(model=Role)
        list_role = [Role(**item) for item in list_role_data]
        list_role_in_db = await repo.insert_many(list_role)
        print(list_role_in_db)
        # Create user
        list_user_data = self.read_file("./seed/1.users/user.json")
        repo = RepositoryFactory().get_repository(model=User)
        list_user = [User(**item) for item in list_user_data]
        await repo.insert_many(list_user)
        return True

    def read_file(self, path: str) -> List[ModelType]:
        content = self.file_reader_service.read_file(path)
        object_data = json.loads(content)
        return object_data
    
    async def run_seed(self, models: ModelSeed) -> List[ModelType]:
        try:
            content = self.file_reader_service.read_file(models.path)
            object_data = json.loads(content)
            # Cast each item to model type
            repo = RepositoryFactory().get_repository(model=models.model)
            await repo.insert_many(object_data)
            return True
        except Exception as e:
            logger.error(e)
            return False

