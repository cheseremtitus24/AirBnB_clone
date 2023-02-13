#!/usr/bin/env python3
"""
Once the command is known, argument completion is handled
by methods with the prefix complete_.
This allows you to assemble a list of possible completions
using your own criteria (query a database,
look at at a file or directory on the filesystem, etc.).
In this case, the program has a hard-coded set of “friends”
who receive a less formal greeting than named or anonymous
strangers.
A real program would probably save the list somewhere,
and either read it once and cache the contents to be
scanned as needed.
Module console
This is a commandline interpreter for backend use by the Developer to perform
specific tasks on data manipulation to a Json file
"""

import cmd
import sys
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example.
    It does not make use of the default help
    which is derived from a function docstring
    rather it reads from help_*funcname*"""

    prompt = '(hbtn) '

    FRIENDS = ['Alice', 'Adam', 'Barbara', 'Bob']
    # Saves all Classes in form a List
    CLASSES = list(storage.classes())
    CLASS_IDS = list()

    def data_validator(self, line):
        """ Validates to verify that proper data is fed to functions"""
        # checks if class name is missing/empty
        if not line:
            print("** class name missing **")
            return False
        # checks that args(class Name) Exists
        elif line not in storage.classes():
            print("** class doesn't exist **")
            return False
        return True

    def do_create(self, args):
        """ Creates a Class Instance and Saves to Storage:
            (hbnb) create User
            """
        if self.data_validator(args):
            # Instantiate the new class and save to storage
            st = storage.classes()[args]()
            # above is similar to calling
            # st = BaseModel()

            st.save()
            print(st.id)

    def do_EOF(self, line):
        """
        This handles case when CTRL-D is pressed and
        cause a successful exit without throwing off an error
        """
        return True

    def do_quit(self, line):
        """ Exits the program """
        return True

    def help_quit(self):
        """
        Provides the helper text that explains what the quit function does
        """
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Skips when an empty line is passed as a commandline argument """
        pass

    def postloop(self):
        """ This function is executed when cmdloop ends
        thus add a new line at end
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
