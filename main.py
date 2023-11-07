#!/usr/bin/python3
from models.base_model import BaseModel

r1 = BaseModel()

r1.name = "Omni man"
print(r1.__dict__)
print("---------------\n")
print(r1)
print("---------------\n")
print(dir(BaseModel()))
print("---------------\n")
print(r1.to_dict())

