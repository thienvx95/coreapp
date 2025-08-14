from pydantic import BaseModel

class OAuth2PasswordRequestForm(BaseModel):
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