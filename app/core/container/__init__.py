from app.business.application_info.services.application_info_service import ApplicationInfoService
from dependency_injector import containers, providers
from app.business.account.schema.user import User
from app.business.account.service.user_service import UserService
from app.business.account.service.role_service import RoleService
from app.business.menu.services.menu_service import MenuService
from app.business.permission.services.permission_service import PermissionService
from app.business.setting.services.setting_service import SettingService
from app.business.common.services.file_reader.file_reader_service import FileReaderService
from app.business.seed.services.mongo_seed_service import MongoSeeder
from app.business.auth.services.auth_service import AuthService
from app.core.data.db_factory import DBFactory
from app.business.application_info.entities.application_info import ApplicationInfo
from app.business.common.entities.migration_db.migration_db import MigrationDB
from app.core.data.repository_factory import RepositoryFactory

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["app.business.application_info.services"]
    )
    
    db_provider = providers.Singleton(DBFactory)
    async_database = providers.Callable(lambda: DBFactory().get_provider().get_database())

    application_info_service = providers.Factory(
        ApplicationInfoService
    )
    user_service = providers.Factory(
        UserService
    )
    role_service = providers.Factory(
        RoleService
    )
    permission_service = providers.Factory(
        PermissionService
    )
    menu_service = providers.Factory(
        MenuService
    )
    setting_service = providers.Factory(
        SettingService
    )
    file_reader_service = providers.Factory(
        FileReaderService
    )
    auth_service = providers.Factory(
        AuthService,
        user_service=user_service
    )
    mongo_seeder = providers.Factory(
        MongoSeeder,
        file_reader_service=file_reader_service
    )