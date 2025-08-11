from fastapi import APIRouter
from app.business.common.api.v1 import health
from app.business.user.api.v1 import auth
from app.business.roles.api.v1 import roles
from app.business.menu.api.v1 import menu
from app.business.permission.api.v1 import permission
from app.business.setting.api.v1 import setting
from app.business.common.view_model import RouteRegister
from app.business.seed.api.v1 import seed
from app.business.user.api.v1 import users
from app.business.application_info.api.v1 import application_info

v1_routers = [
    RouteRegister(health.router, "/health", ["Health"]),
    RouteRegister(auth.router, "/auth", ["Auth"]),
    RouteRegister(users.router, "/users", ["Users"]),
    RouteRegister(roles.router, "/roles", ["Roles"]),
    RouteRegister(permission.router, "/permissions", ["Permissions"]),
    RouteRegister(menu.router, "/menus", ["Menus"]),
    RouteRegister(setting.router, "/settings", ["Settings"]),
    RouteRegister(seed.router, "/seed", ["Seed"]),
    RouteRegister(application_info.router, "/application", ["Application"]),
]

api_router = APIRouter()

for v1_router in v1_routers:
    api_router.include_router(router=v1_router.route, prefix=v1_router.prefix, tags=v1_router.tags)