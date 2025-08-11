from app.business.application_info.services.application_info_service import ApplicationInfoService
from dependency_injector import containers, providers
from app.business.user.services.user_service import UserService
from app.business.roles.services.role_service import RoleService
from app.business.menu.services.menu_service import MenuService
from app.business.permission.services.permission_service import PermissionService
from app.business.setting.services.setting_service import SettingService
from app.business.common.services.file_reader.file_reader_service import FileReaderService
from app.business.seed.services.mongo_seed_service import MongoSeeder
from app.business.user.services.auth_service import AuthService
from app.core.data.mongo_db.mongo_repository import MongoRepository
from app.core.data.db_factory import DBFactory
from app.business.application_info.entities.application_info import ApplicationInfo
from app.business.common.entities.migration_db.migration_db import MigrationDB
from app.business.user.entities.user import User
from app.business.roles.entities.role import Role
from app.business.permission.entities.permission import Permission
from app.business.menu.entities.menu import Menu
from app.business.setting.entities.setting import Setting


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["app.business.application_info.services"]
    )

    db_provider = providers.Singleton(DBFactory)
    async_database = providers.Callable(lambda: DBFactory().get_provider().get_database())
    user_repository = providers.Factory(
        MongoRepository,
        db=async_database,
        collection_name="users",
        model=User
    )

    application_info_repository = providers.Factory(
        MongoRepository,
        db=async_database,
        collection_name="application_info",
        model=ApplicationInfo
    )
    migration_db_repository = providers.Factory(
        MongoRepository,
        db=async_database,
        collection_name="migration_dbs",
        model=MigrationDB
    )
    role_repository = providers.Factory(
        MongoRepository,
        db=async_database,
        collection_name="roles",
        model=Role
    )
    permission_repository = providers.Factory(
        MongoRepository,
        db=async_database,
        collection_name="permissions",
        model=Permission
    )
    menu_repository = providers.Factory(
        MongoRepository,
        db=async_database,
        collection_name="menus",
        model=Menu
    )
    setting_repository = providers.Factory(
        MongoRepository,
        db=async_database,
        collection_name="settings",
        model=Setting
    )

    application_info_service = providers.Factory(
        ApplicationInfoService,
        repository=application_info_repository,
        db_migration_repository=migration_db_repository
    )
    user_service = providers.Factory(
        UserService,
        repository=user_repository
    )
    role_service = providers.Factory(
        RoleService,
        repository=role_repository
    )
    permission_service = providers.Factory(
        PermissionService,
        repository=permission_repository
    )
    menu_service = providers.Factory(
        MenuService,
        repository=menu_repository
    )
    setting_service = providers.Factory(
        SettingService,
        repository=setting_repository
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
