import json

from app.core import logging
from app.core.data.repository_factory import RepositoryFactory
from app.core.data.mongo_db.mongodb import MongoDB
from app.core.logging.logging import logger
from app.business.common.services.file_reader.file_reader_service import FileReaderService
from app.core.container import Container

class MongoSeeder:
    models=[
        {
            "model": "users",
            "path": "./seed/1.users/user.json",
        },
        {
            "model": "roles",
            "path": "./seed/2.roles/role.json",
        },
        {
            "model": "menus",
            "path": "./seed/3.menus/menus.json",
        },
        {
            "model": "settings",
            "path": "./seed/4.settings/setting.json",
        }
    ]

    def __init__(self, file_reader_service: FileReaderService):
        self.file_reader_service = file_reader_service

    def seed(self) -> bool:
        try:
            for model in self.models:
                content = self.file_reader_service.read_file(model["path"])
                object_data = json.load(content)
                # You need to map model["model"] to the actual model class here
                # For now, assuming you have a mapping dict called model_class_map
                repo = Container.generic_repository(collection_name=model["model"], model=model_class_map[model["model"]])
                repo.insert_many(object_data)
            return True
        except Exception as e:
            logging.error(e)
            return False
