#!/usr/bin/python3

"""
    console
    - Module containing command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Commandline interpreter object
    """
    prompt = '(hbnb) '
    def emptyline(self):
        """
            Left with elipsis to override the default implementation
        """
        ...

    def do_quit(self, arg):
        """quit - exits the program"""
        exit()

    def do_EOF(self, arg):
        """EOF - exits the program"""
        exit()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
