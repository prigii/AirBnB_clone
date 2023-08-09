#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    intro = "Welcome to AirBnB Console CLI. Type 'help' for available commands"
    prompt = "(hbnb)"
    def do_quit(args, line):
        """Quits the command interpreter""" 
        print("logout")
        return True
    def do_help(self, arg: str) -> bool | None:
        """Type help <topic> to get help on different commands"""
        return super().do_help(arg)
    def do_eof(self, line):
        """Handle EOF"""
        print("Exiting the CLI")
        return True
    def default(self, line: str) -> None:
        return super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()