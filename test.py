from pydantic import BaseModel
import os


class Jp(BaseModel):
    name: str
    age: int


def test():
    a = 12
