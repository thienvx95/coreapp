from fastapi import APIRouter, Depends
from app.business.seed.services.seed_service import SeederService
from app.core.container import Container

router = APIRouter()

def get_seed_service() -> SeederService:
    """
    Get the setting service instance.
    """
    return Container.seeder_service()


@router.post("/run-seed")
async def run_seed(seed_service: SeederService = Depends(get_seed_service)) -> bool:
    return await seed_service.seed()