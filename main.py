#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review

u1 = User()
r1 = Review()
print(u1,"\n\n", r1)

"""x = "BaseModel"
r1 = eval("{}()".format(x))
r2 = BaseModel()
r1.name = "Omni man"
print(r1.__dict__)
print("---------------\n")
print(r1)
#print("---------------\n")
print(r1.to_dict())
print("---------------\n")
f1 = FileStorage()
print(f1.all())
f1.new(r1)
f1.new(r2)
print(f1.all())
f1.reload()
print("Reload method:")
for key in f1.all():
    print(f1.all()[key].__dict__)
    print("-------------------")
"""

