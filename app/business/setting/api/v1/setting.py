from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.business.setting.services.setting_service import SettingService
from app.business.setting.view_model.setting_viewmodel import SettingCreate, SettingUpdate
from app.business.setting.entities.setting import Setting
from app.core.container import Container

router = APIRouter()

def get_setting_service() -> SettingService:
    """
    Get the setting service instance.
    """
    return Container.setting_service()

@router.post("/", response_model=Setting, status_code=status.HTTP_201_CREATED)
async def create_setting(
    setting_in: SettingCreate,
    setting_service: SettingService = Depends(get_setting_service)
) -> Setting:
    """
    Create a new setting.
    """
    # Check if setting with name exists
    if await setting_service.get_by_name(setting_in.name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Setting with this name already exists"
        )
    
    return await setting_service.create(setting_in)

@router.get("/", response_model=List[Setting])
async def list_settings(
    skip: int = 0,
    limit: int = 10,
    setting_service: SettingService = Depends(get_setting_service)
) -> List[Setting]:
    """
    List settings with pagination.
    """
    return await setting_service.list(skip=skip, limit=limit)

@router.get("/public", response_model=List[Setting])
async def get_public_settings(
    setting_service: SettingService = Depends(get_setting_service)
) -> List[Setting]:
    """
    Get all public settings.
    """
    return await setting_service.get_public_settings()

@router.get("/group/{group}", response_model=List[Setting])
async def get_settings_by_group(
    group: str,
    setting_service: SettingService = Depends(get_setting_service)
) -> List[Setting]:
    """
    Get all settings in a specific group.
    """
    return await setting_service.get_by_group(group)

@router.get("/section/{section}", response_model=List[Setting])
async def get_settings_by_section(
    section: str,
    setting_service: SettingService = Depends(get_setting_service)
) -> List[Setting]:
    """
    Get all settings in a specific section.
    """
    return await setting_service.get_by_section(section)

@router.get("/group/{group}/section/{section}", response_model=List[Setting])
async def get_settings_by_group_and_section(
    group: str,
    section: str,
    setting_service: SettingService = Depends(get_setting_service)
) -> List[Setting]:
    """
    Get all settings in a specific group and section.
    """
    return await setting_service.get_by_group_and_section(group, section)

@router.get("/{setting_id}", response_model=Setting)
async def get_setting(
    setting_id: str,
    setting_service: SettingService = Depends(get_setting_service)
) -> Setting:
    """
    Get a setting by ID.
    """
    if setting := await setting_service.get(setting_id):
        return setting
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Setting not found"
    )

@router.get("/name/{name}", response_model=Setting)
async def get_setting_by_name(
    name: str,
    setting_service: SettingService = Depends(get_setting_service)
) -> Setting:
    """
    Get a setting by name.
    """
    if setting := await setting_service.get_by_name(name):
        return setting
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Setting not found"
    )

@router.put("/{setting_id}", response_model=Setting)
async def update_setting(
    setting_id: str,
    setting_in: SettingUpdate,
    setting_service: SettingService = Depends(get_setting_service)
) -> Setting:
    """
    Update a setting.
    """
    if setting := await setting_service.update(setting_id, setting_in):
        return setting
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Setting not found"
    )

@router.delete("/{setting_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_setting(
    setting_id: str,
    setting_service: SettingService = Depends(get_setting_service)
) -> None:
    """
    Delete a setting.
    """
    if not await setting_service.delete(setting_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Setting not found"
        )