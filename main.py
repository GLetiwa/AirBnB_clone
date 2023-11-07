#!/usr/bin/python3
from models.base_model import BaseModel

r1 = BaseModel()

print(f'id = {r1.id}\ncreated_at = {r1.created_at}\nupdated_at = {r1.updated_at}')
print(r1.__dict__)
print(r1)
print(dir(BaseModel()))
print(r1.to_dict())

