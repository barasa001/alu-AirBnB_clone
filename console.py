#!/usr/bin/python3
"""Command line interpreter"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """for the prompt"""

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """For the end of the file"""
        return True

    def do_quit(self, file):
        """To exit the program"""
        sys.exit()

    def emptyline(self):
        """for overwriting"""
        print('', end="")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

