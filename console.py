#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    intro = "Welcome to AirBnB Console CLI. Type 'help' for available commands"
    prompt = "(hbnb)"
    all_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        
    def do_create(self, arg):
        """Creates a new instance of the BaseModel, saves it and prints the ID"""
        args = arg.split()
        if self.valid(arg):
            new = BaseModel()
            print(new.id)
            new.save()
        if len(args[0]) not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 0:
            print("** class name missing **")
            return
        else:
            print("** no instance found **")
            return
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if self.valid(arg):
            new = BaseModel()
            print(new.id)
        if len(args[0]) is not HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            print("** no instance found **")
            return
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        #if self.valid(arg, True):
         #   Key = '.'.join(arg.split()[:2])
        #    del storage.all()
          #  storage.save()"""
        
        args = arg.split()
        if len(args[0]) is not HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            print("** no instance found **")
            return
        
    def do_all(self, arg: str):
        """Prints all string representation of all instances"""
        args = arg.split()
        if args[0] in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
    def do_count(self, arg):
        args = arg.split()
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.all_classes():
            print("** class doesn't exist **")
        else:
            count = [key for key in storage.all() if 
                     key.startswith(args[0] + '.')]
            print(len(count))

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args=arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(args)==1:
            print("** instance id missing **")
            return
        if len(args)==2:
            print("** attribute name missing **")
            return
        if len(args)==3:
            print("** value missing **")
            return
        valid_ids = []
        id = args[1]
        objects_dict = storage.all()
        for key in objects_dict:
            class_name, inst_id = key.split(".")
            valid_ids.append(inst_id)
            if id in valid_ids:
                obj = objects_dict[f"{class_name}.{id}"]
        else:
            print("** no instance found **")


              
        
         

    
    def do_quit(args, line):
        """Quits the command interpreter""" 
        print("logout")
        return True
    def do_help(self, arg: str) -> bool | None:
        """Type help <topic> to get help on different commands"""
        return super().do_help(arg)
    def do_EOF(self, line):
        """Handle EOF"""
        print("Exiting the CLI")
        return True
    def default(self, line: str) -> None:
        return super().default(line)
    



if __name__ == '__main__':
    HBNBCommand().cmdloop()