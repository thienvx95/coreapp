from pydantic import BaseModel

class RunSeedResponse(BaseModel):
    success: bool
    message: str