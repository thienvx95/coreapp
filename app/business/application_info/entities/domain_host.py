from pydantic import Field, BaseModel

class DomainHost(BaseModel):
    name: str = Field(..., description="Host name")
    port: int = Field(..., description="Domain port")
    language: str = Field(..., description="Domain language")
    domain: str = Field(..., description="Domain name")
    scheme: str = Field(..., description="Domain scheme")
    primary: bool = Field(..., description="Domain primary")
