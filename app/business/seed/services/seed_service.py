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
    def __init__(self, file_reader_service: FileReaderService):
        self.file_reader_service = file_reader_service

    async def seed(self) -> bool:
        try:
            role_repo = RepositoryFactory().get_repository(model=Role)
            user_repo = RepositoryFactory().get_repository(model=User)
            menu_repo = RepositoryFactory().get_repository(model=Menu)
            setting_repo = RepositoryFactory().get_repository(model=Setting)

            if(await role_repo.find_one({"name": "Admin"}) is None):
                # Create role
                list_role_data = self.read_file("./seed/2.roles/role.json")
                list_role = [Role(**item) for item in list_role_data]
                list_role_in_db = await role_repo.insert_many(list_role)
            
            else:
                list_role_in_db = await role_repo.find_many({})
            admin_role = list(filter(lambda x: x.name == "Admin", list_role_in_db))[0]
            
            # Create user
            if(await user_repo.find_one({"username": "admin"}) is None):
                print("admin_user is None")
                list_user_data = self.read_file("./seed/1.users/user.json")
                list_user = [User(**item) for item in list_user_data]
                admin_user = list(filter(lambda x: x.username == "admin", list_user))[0]
                admin_user.roles.append(admin_role)
                await user_repo.insert_many(list_user)

            # Create menu
            if(await menu_repo.find_one({"key": "DASHBOARD_ADMIN"}) is None):
                list_menu_data = self.read_file("./seed/3.menus/menus.json")
                list_menu = []
                for item in list_menu_data:
                    item["roles"] = [admin_role]
                    menu = Menu(**item)
                    list_menu.append(menu)

                await menu_repo.insert_many(list_menu)

            # Create setting
            if(await setting_repo.find_one({"key": "DASHBOARD_ADMIN"}) is None):
                list_setting_data = self.read_file("./seed/4.settings/setting.json")
                list_setting = [Setting(**item) for item in list_setting_data]
                await setting_repo.insert_many(list_setting)

        except Exception as e:
            logger.error(e)
            return False
        return True
        
    def read_file(self, path: str) -> List[ModelType]:
        content = self.file_reader_service.read_file(path)
        object_data = json.loads(content)
        return object_data
    
    async def run_seed(self, models: List[ModelSeed]) -> List[ModelType]:
        try:
            for model in models:
                content = self.file_reader_service.read_file(model.path)
                object_data = json.loads(content)
                # Cast each item to model type
                list_object_data = [model.model(**item) for item in object_data]
                repo = RepositoryFactory().get_repository(model=model.model)
                print(list_object_data)
                await repo.insert_many(list_object_data)

            return True
        except Exception as e:
            logger.error(e)
            return False

