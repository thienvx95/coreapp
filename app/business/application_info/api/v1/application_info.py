from fastapi import APIRouter, Depends, HTTPException, status

from app.business.application_info.entities import ApplicationInfo
from app.business.application_info.services import ApplicationInfoService
from app.core.container import Container

router = APIRouter()

def get_application_info_service() -> ApplicationInfoService:
    """
    Get the setting service instance.
    """
    return Container.application_info_service()


@router.get("/application-info", response_model=ApplicationInfo)
async def application_info(application_info_service: ApplicationInfoService = Depends(get_application_info_service)) -> ApplicationInfo:
    info = await application_info_service.get_application_info()
    if info is None:
        # If the service returns None, it means the application info was not found.
        # Raise an HTTPException with status code 404.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application info not found")
    return info

