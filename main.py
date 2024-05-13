from pydantic import BaseModel


class Stats(BaseModel):
    mean: float
    min: float


stat = Stats(mean=12, min=1)

print(stat.model_dump_json())
