from fastapi import APIRouter, Depends

from app.core.services.factory import ServiceFactory
from app.core.services.mongo_seed.mongo_seed_service import MongoSeeder

router = APIRouter()

def get_mongo_seed_service() -> MongoSeeder:
    """
    Get the setting service instance.
    """
    return ServiceFactory.get_service(MongoSeeder)


@router.post("/run-seed")
async def run_seed(mongo_seed_service: MongoSeeder = Depends(get_mongo_seed_service)) -> bool:
    return await mongo_seed_service.seed()