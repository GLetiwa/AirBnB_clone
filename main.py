#!/usr/bin/python3
"""from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

x = "BaseModel"
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

from console import HBNBCommand

h1 = HBNBCommand()

h1.convert_dict('''"38f22813-2753-4d42-b37c-57a17f1e4f88",
{'first_name': "John", "age": 89}''', 'BaseModel')
