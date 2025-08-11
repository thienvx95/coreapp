from app.core.data.model_type import ModelType


class ModelSeed:
    def __init__(self, model: ModelType, path: str):
        self.model = model 
        self.path = path
    model: ModelType
    path: str
