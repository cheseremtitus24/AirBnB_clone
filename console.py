#!/usr/bin/env python3
"""
Module console
This is a commandline interpreter for backend use by the Developer to perform
specific tasks on data manipulation to a Json file
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example.
    It does not make use of the default help
    which is derived from a function docstring
    rather it reads from help_*funcname*"""

    prompt = '(hbnb) '

    FRIENDS = ['Alice', 'Adam', 'Barbara', 'Bob']

    def do_create(self, args):
        """ Creates a Class Instance and Saves to Storage:
            (hbnb) create User
            """

        # checks if class name is missing/empty
        if not line:
            print("** class name missing **")
        # checks that args(class Name) Exists
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            # Instantiate the new class and save to storage
            st = storage.classes()[args]()
            st.save()
            print(st.id)

    def do_greet(self, person):
        'This help msg is overriden by help_greet'
        if person and person in self.__class__.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "hello," + person
        else:
            greeting = 'hello'
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        """ Perfoms argument autocompletions """
        if not text:
            completions = self.__class__.FRIENDS[:]
        else:
            completions = [f for f in self
                           .__class__.FRIENDS if f.startswith(text)]
        return completions

    def help_greet(self):
        """ prints a properly formatted help text for greet command
        and overrrides the default do_greet docstring """
        print("\n".join(['greet [person]', '\t\tGreet the named person', ]))

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
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
