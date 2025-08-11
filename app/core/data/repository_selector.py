from app.core.config import settings
from app.core.data.mongo_db.mongo_repository import MongoRepository

def get_repository_class():
    if settings.DB_PROVIDER.lower() == "mongodb":
        return MongoRepository
    # Add more DB providers here as needed
    raise NotImplementedError("No repository class for this DB provider") 
