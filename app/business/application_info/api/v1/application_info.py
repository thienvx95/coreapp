from fastapi import APIRouter, Depends

from app.business.application_info.services.application_info_service import ApplicationInfoService
from app.core.services.factory import ServiceFactory

router = APIRouter()

def get_application_info_service() -> ApplicationInfoService:
    """
    Get the setting service instance.
    """
    return ServiceFactory.get_service(ApplicationInfoService)


@router.post("/application-info")
async def application_info(application_info_service: ApplicationInfoService = Depends(get_application_info_service)) -> bool:
    return await application_info_service.get_application_info()