from pydantic import BaseModel


class MockInput(BaseModel):
    endpoint: str
    prompt: str

    class Config:
        schema_extra = {
            "example": {
                "endpoint": "pokemon",
                "prompt": "Quiero una lista de 10 pokemones"
            }
        }
