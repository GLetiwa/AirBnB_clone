#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

"""x = "BaseModel"
r1 = eval("{}()".format(x))
r2 = BaseModel()
r1.name = "Omni man"
print(r1.__dict__)
print("---------------\n")
print(r1)
#print("---------------\n")
print(r1.to_dict())
print("---------------\n")"""
f1 = FileStorage()
"""print(f1.all())
f1.new(r1)
f1.new(r2)
print(f1.all())"""
f1.reload()
print("Reload method:")
for key in f1.all():
    print(f1.all()[key].__dict__)
    print("-------------------")
