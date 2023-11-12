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

from models.place import Place
kw = {'id': '6c4be621-c544-48b9-9070-47c01ef07259', 'created_at': '2023-11-12T22:57:14.555572', 'updated_at': '2023-11-12T22:57:14.555572', 'city_id': '', 'user_id': '', 'name': '', 'description': '', 'number_rooms': 0, 'max_guest': 20, 'price_by_night': 10, 'latitude': 110.0, 'longitude': 10.0, 'amenity_ids': [], '__class__': 'Place'}
p1 = Place()
print(p1.to_dict())
