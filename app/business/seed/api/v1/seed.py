from fastapi import APIRouter, Depends
from app.business.seed.services.mongo_seed_service import MongoSeeder
from app.core.container import Container

router = APIRouter()

def get_mongo_seed_service() -> MongoSeeder:
    """
    Get the setting service instance.
    """
    return Container.mongo_seeder()


@router.post("/run-seed")
async def run_seed(mongo_seed_service: MongoSeeder = Depends(get_mongo_seed_service)) -> bool:
    return await mongo_seed_service.seed()