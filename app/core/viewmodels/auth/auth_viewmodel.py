from pydantic import BaseModel

class LoginRequest(BaseModel):
    """
    Login request model.
    """
    username: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "secretpassword"
            }
        } 