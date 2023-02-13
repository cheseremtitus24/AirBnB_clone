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

    def complete_create(self, text, line, begidx, endidx):
        """ Perfoms argument autocompletions """
        if not text:
            completions = self.__class__.CLASSES[:]
        else:
            completions = [f for f in storage.classes() if f.startswith(text)]
        return completions

    def help_greet(self):
        """ prints a properly formatted help text for greet command
        and overrrides the default do_greet docstring """
        print("\n".join(['greet [person]', '\t\tGreet the named person', ]))

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
            completions = [
                f for f in self.__class__.FRIENDS if f.startswith(text)]
        return completions

    def do_show(self, args):
        """ Prints the string representation of an instance
        based on class name and id
            (hbnb) show BaseModel ee49c413-023a-4b49-bd28-f2936c95460d
            """
        if not args:
            """

            """
            print("** class name missing **")
        else:
            words = args.split(" ")
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def complete_show(self, text, line, begidx, endidx):
        """ Perfoms Class and ID autocompletions
            (hbnb) show BaseModel ee49c413-023a-4b49-bd28-f2936c95460d
        """
        if not text:
            completions = self.__class__.CLASSES[:]
        else:
            completions = [f for f in storage.classes() if f.startswith(text)]
        return completions

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
            (hbnb) destroy BaseModel ee49c413-023a-4b49-bd28-f2936c95460d
        """
        if not args:
            print("** class name missing **")

        else:
            words = args.split(" ")
            if words[0] not in self.__class__.CLASSES[:]:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                # print("all items in storage", storage.all())
                # print()
                # Todo: The keys keep changing when console is restarted
                # but print it from storage restores the original
                # print(" all keys are ",list(storage.all()))
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def complete_destroy(self, text, line, begidx, endidx):
        """ Perfoms Class and ID autocompletions
            (hbnb) destroy BaseModel ee49c413-023a-4b49-bd28-f2936c95460d
        """
        if not text:
            completions = self.__class__.CLASSES[:]
        else:
            completions = [f for f in storage.classes() if f.startswith(text)]
        return completions

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the
        class name
            (hbnb) all BaseModel
            # also
            (hbnb) all
        """
        print_list = list()
        if args:
            words = args.split(' ')
            classname = words[0]
            if classname not in self.__class__.CLASSES[:]:
                print("** class name missing **")
            else:
                # iterate through storage class items
                for key, cls_obj in storage.all().items():
                    if type(cls_obj).__name__ == classname:
                        print_list.append(str(cls_obj))
                print(print_list)
        else:
            # iterate through storage class items: print all
            for key, cls_obj in storage.all().items():
                print_list.append(str(cls_obj))
            print(print_list)

    def complete_all(self, text, line, begidx, endidx):
        """ Perfoms Class and ID autocompletions
            (hbnb) all BaseModel
            (hbnb) all
        """
        if not text:
            completions = self.__class__.CLASSES[:]
        else:
            completions = [f for f in storage.classes() if f.startswith(text)]
        return completions

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). Ex:
        (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        if not args:
            print("** class name missing **")

        else:
            words = args.split(" ")
            # checks if classname exists
            if words[0] not in self.__class__.CLASSES[:]:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")

            key = "{}.{}".format(words[0], words[1])
            if key not in storage.all():
                print("** no instance found **")

            elif len(words) < 3:
                print("** attribute name missing **")
            elif len(words) < 4:
                print("** value missing **")
            # ignores addition of other arguments
            else:
                value = words[3]
                attribute = words[2]
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[words[0]]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def complete_update(self, text, line, begidx, endidx):
        """ Perfoms Class and ID autocompletions
            (hbnb) update BaseModel 13-023-4b-b8-fd email "airbnb@mail.com"
        """
        if not text:
            completions = self.__class__.CLASSES[:]
        else:
            completions = [f for f in storage.classes() if f.startswith(text)]
        return completions

    def help_greet(self):
        """ prints a properly formatted help text for greet command
        and overrrides the default do_greet docstring """
        print("\n".join(['greet [person]', '\t\tGreet the named person', ]))

    def do_EOF(self, line):
        """ This handles case when CTRL-D is pressed and
        cause a successful exit without throwing off an error"""
        return True

    def do_quit(self, line):
        """ Exits the program """
        return True

    def emptyline(self):
        """Skips when an empty line is passed as a commandline argument """
        pass

    def postloop(self):
        """ This function is executed when cmdloop ends
        thus add a new line at end
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
