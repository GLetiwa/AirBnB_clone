#!/usr/bin/python3

"""
    console
    - Module containing command interpreter
"""
import cmd
import sys
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        Commandline interpreter object
    """
    prompt = '(hbnb) '
    all_classes = ['BaseModel', 'User', 'State', 'City',
                   'Amenity', 'Place', 'Review']

    def emptyline(self):
        """
            Left with elipsis to override the default implementation
        """
        ...

    def do_quit(self, arg):
        """quit - Exits the console"""

        sys.exit()

    def do_EOF(self, arg):
        """EOF - Exits the console"""
        print("")
        sys.exit()

    def default(self, arg):

        string = HBNBCommand.args_check(arg)

        if (string is None):
            return
        
        else:
            obj, command, param = string
        
        if (command != 'count'):
            func = eval("self.do_{}".format(command))
        
        if (command == "all"):
            func(obj)

        elif (command in ["show", "destroy"]):
            param = "{} {}".format(obj, param.strip('"'))
            func(param)
        
        elif (command == "update"):
            id_dict = HBNBCommand.convert_dict(param)

            if (id_dict):
                id_no, d_attr = id_dict

                for key in d_attr:
                    string = "{} {} {} {}".format(obj, id_no, key, d_attr[key])
                    self.do_update(string)


        else:
            HBNBCommand.count(obj)

    @classmethod
    def args_check(cls, arg):
        string = re.fullmatch(r"(.+)\.([a-z]{3,7})\((.*)\)", arg)
        commands = ['all', 'count', 'show', 'destroy', 'update']

        #syntax and command check
        if (string is None or string.group(2) not in commands):
            print("*** Unknown syntax: {}".format(arg))
            return

        #obj check
        if (string.group(1) not in cls.all_classes):
            print("** class doesn't exist **")
            return
        
        #instance check
        if (string.group(3) == "" and string.group(2) in commands[2:]):
            print("** instance id missing **")
            return
        
        #all & count check
        if (string.group(3) != "" and string.group(2) in commands[:2]):
            print("*** Unknown syntax: {}".format(arg))
            return
        
        return (string.groups())

    """def default(self, arg):
        " default - Interpret instance based commands "
        commands = ['all', 'show', 'destroy', 'update']

        string = re.fullmatch(r'([A-Za-z]{4,9})\.([a-z]{3,7})\(("?.*"?)\)', arg)

        obj, command, param = string.groups()
        
        #print(obj, "|", command, "|", param)
        if obj in self.all_classes and command in commands:
            func = eval("self.do_{}".format(command))

            if (command in ['show', 'destroy']):
                param = string.group(3).strip('"')
                func("{} {}".format(obj, param))

            elif (command == 'all' and param == ''):
                func(obj)

            elif (command == 'update'):
                try:
                    id_no, attraram = HBNBCommand().convert_dict(param)
                except (ValueError):
                    return
                
                for key in attraram:
                    string = '{} {} {} "{}"'.format(obj, id_no, key, attraram[key])
                    self.do_update(string)
            else:
                print("*** Unknown syntax: {}".format(arg))
        else:
            print("*** Unknown syntax: {}".format(arg))"""

    def do_create(self, arg):
        "create- Creates & saves an Object(to a JSON file) & prints it's ID"

        if (arg in self.all_classes):
            obj = eval("{}()".format(arg))
            storage.new(obj)
            storage.save()
            print(obj.id)
        elif (arg == ''):
            print('** class name missing **')
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        "show - Prints a string representation of an instance"

        id_string = HBNBCommand.general_check(arg)

        if (id_string is not None):
            print(storage.all().get(id_string))

    def do_destroy(self, arg):
        "destroy - Destroys an instance & removes it from the JSON file"

        id_string = HBNBCommand.general_check(arg)

        if (id_string is not None):
            del storage.all()[id_string]
            storage.save()

    def do_all(self, arg):
        "all - prints all string representation of all/specified instances"

        if (arg == "") or (arg in self.all_classes):
            for key in storage.all():
                if (arg in key):
                    print(storage.all()[key])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        "update - Updates an instance"

        params = arg.split()

        if (len(params) > 3):
            id_string = HBNBCommand.general_check(" ".join(params[:2]))

            if (id_string is not None):

                x = storage.all()[id_string]
                rem_str = " ".join(params[3:])
                value = rem_str.split('"')[1]

                setattr(x, params[2], value)

        else:
            if (len(params) < 3):
                parse_arg = arg
                err_string = "** attribute name missing **"

            else:
                parse_arg = " ".join(arg.split()[:2])
                err_string = "** value missing **"

            id_string = HBNBCommand.general_check(parse_arg)

            if (id_string is not None):
                print(err_string)

    @classmethod
    def general_check(cls, arg):
        if (arg == ''):
            print('** class name missing **')

        elif (arg.split()[0] in cls.all_classes):
            params = arg.split()
            id_string = ".".join(params)

            if len(params) > 1:
                if (id_string in storage.all()):
                    return (id_string)
                else:
                    print("** no instance found **")

            else:
                print("** instance id missing **")

        else:
            print("** class doesn't exist **")
        return (None)

    @staticmethod
    def convert_dict(params):
        dict_args = dict()
        d_keys = storage.all().keys()

        id_no = re.search(r'^"([^"]*)"', params)
        attr = re.search(r'^"[^"]*", "([\w]+)"', params)
        value = re.search(r'^"[^"]*", "[\w]+", (.*)', params)
        str_dict = re.search(r'^"[^"]*", (\{.+})', params)

        if (id_no is not None):
            if (str_dict is not None):

                return (id_no.group(1), str_dict.group(1))

            elif (attr is not None):
                if (value):
                    dict_args = {attr.group(1) : value.group(1)}
                    return (id_no.group(1),dict_args)
                
                else:
                    print('** value missing **')
                    return

            else:
                print('** attribute name missing **')
                return
        else:
            print('** no instance found **')

    @classmethod
    def count(cls, arg):
        "count - prints number of existing specified instance"

        value = 0
        if (arg == "") or (arg in cls.all_classes):
            for key in storage.all():
                if (arg in key):
                    value += 1
            print(value)
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
