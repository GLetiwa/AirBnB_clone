#!/usr/bin/python3

"""
    console
    - Module containing command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        Commandline interpreter object
    """
    prompt = '(hbnb) '
    all_classes = ['BaseModel']

    def emptyline(self):
        """
            Left with elipsis to override the default implementation
        """
        ...

    def do_quit(self, arg):
        """quit - Exits the program"""
        exit()

    def do_EOF(self, arg):
        """EOF - Exits the program"""
        exit()

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
        "all - prints all string representation of all instances"

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
