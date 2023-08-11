#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import json
'''
    This is the console for the AirBnB clone project
'''


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone"""

    prompt = "(hbnb)"
    all_classes = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]

    def do_create(self, arg):
        """Creates a new instance of the BaseModel, saves it
          and prints the ID"""
        args = arg.split()
        if args:
            if args[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return
            else:
                new = storage.classes()[args[0]]()
                print(new.id)
                new.save()
        else:
            print("** class name missing **")
            return

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = arg.split()
        if args:
            if args[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif len(args) == 2:
                dicts = storage.all()
                for key, value in dicts.items():
                    if (str(args[0]) + '.' + str(args[1])) == key:
                        print(str(value))
                        return
                print("** no instance found **")
                return
        else:
            print("** class name missing **")
            return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if args:
            if args[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif len(args) == 2:
                dicts = storage.all()
                for key in dicts.keys():
                    if (str(args[0]) + '.' + str(args[1])) == key:
                        dicts.pop(key)
                        return
                print("** no instance found **")
                return
        else:
            print("** class name missing **")
            return

    def do_all(self, arg: str):
        """Prints all string representation of all instances"""
        listofdicts = []
        args = arg.split('.')
        if args[0]:
            if len(args) > 0 and args[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return
            else:
                dicts = storage.all()
                for key, value in dicts.items():
                    if args[0] == value.__class__.__name__:
                        listofdicts += [str(value)]
                print(listofdicts)
        else:
            dicts = storage.all()
            for key, value in dicts.items():
                listofdicts += [str(value)]
            print(listofdicts)

    def do_update(self, arg):
        """Updates an instance based on the class name
          and id by adding or updating attribute"""
        args = arg.split()
        if args:
            if args[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return
            else:
                dicts = storage.all()
                for key, value in dicts.items():
                    if (str(args[0]) + '.' + str(args[1])) == key:
                        setattr(value, args[2], args[3])
                        value.save()
                        return
        else:
            print("** class name missing **")
            return

    def do_quit(args, line):
        """Quits the command interpreter"""
        return True

    def do_help(self, arg: str) -> bool | None:
        """Type help <topic> to get help on different commands"""
        return super().do_help(arg)

    def do_EOF(self, line):
        """Handle EOF"""
        print()
        return True

    def emptyline(self) -> bool:
        return False

    def default(self, line: str) -> None:
        return super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
