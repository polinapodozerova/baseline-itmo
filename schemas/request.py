from pydantic import BaseModel

class PredictionRequest(BaseModel):
    id: int
    query: str

class PredictionResponse(BaseModel):
    id: int
    answer: int
    reasoning: str
    sources: list[str]