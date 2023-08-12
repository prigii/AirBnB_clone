#!/usr/bin/env python3
'''
    This is the console for the AirBnB clone project
     A command-line interpreter for managing objects within
    an HBNB data storage system.
'''
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand class

    A command-line interpreter for managing objects within
    an HBNB data storage system.

    Attributes:
        prompt (str): The command prompt string.
        all_classes (list): A list of available class names for object management.
    """

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

    def help_create(self):
        """
        Display help information for the create command.
        """
        print("\nUsage: create <class_name>\n")
        print("This command creates a new instance of", end=" ")
        print("the specified class and assigns it a unique identifier.\n")

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

    def help_show(self):
        """
        Display help information for the show command.
        """
        print("\nUsage: show <class_name> <id>\n")
        print("This command displays an instance's string representation.\n")

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

    def help_destroy(self):
        """
        Display help for the destroy command.
        """
        print("\nUsage: help destroy\n")
        print("Destroy command deletes an instance by class", end=' ')
        print("name and instance ID.\n")

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

    def help_all(self):
        """
        Display help for the all command.
        """
        print("\nUsage: help all\n")
        print("All command displays string representations of all instances.")
        print("Optionally, provide a class name to filter instances", end=' ')
        print("of a specific class.\n")

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

    def help_update(self):
        """
        Display help for the update command.
        """
        print("\nUsage: help update\n")
        print("Update command modifies an instance's attribute value", end=" ")
        print("by class name, instance ID, attribute name, and value.")
        print("Provide required arguments to update.\n")

    def do_quit(args, line):
        """Quits the command interpreter"""
        return True

    def help_quit(self):
        """
        Display help information for the quit command.
        """
        print("\nUsage: quit\n")
        print("This command allows you to exit the command", end=" ")
        print("interpreter gracefully.\n")

    def do_help(self, arg: str) -> bool | None:
        """Type help <topic> to get help on different commands"""
        return super().do_help(arg)

    def do_EOF(self, line):
        """Handle EOF"""
        print()
        return True

    def help_EOF(self):
        """
        Display help information for the EOF command.
        """
        print("\nUsage: EOF\n")
        print("This command allows you to exit the command", end=" ")
        print("interpreter gracefully by pressing Ctrl+D (EOF).\n")

    def emptyline(self):
        '''Do nothing on empty line'''
        pass

    def default(self, line: str):
        '''Default behavior for cmd module when no command is found'''
        return super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
