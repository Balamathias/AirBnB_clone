#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        regex_match = re.search(r"\.", arg)
        if regex_match is not None:
            arg_len = [arg[:regex_match.span()[0]], arg[regex_match.span()[1]:]]
            regex_match = re.search(r"\((.*?)\)", arg_len[1])
            if regex_match is not None:
                command = [arg_len[1][:regex_match.span()[0]], regex_match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(arg_len[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_show(self, arg):
        """
        Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arg_len = parse(arg)
        obj_dict = storage.all()
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_len) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_len[0], arg_len[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_len[0], arg_len[1])])

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        arg_len = parse(arg)
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_len[0])().id)
            storage.save()

    def do_destroy(self, arg):
        """
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """
        arg_len = parse(arg)
        obj_dict = storage.all()
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_len) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_len[0], arg_len[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_len[0], arg_len[1])]
            storage.save()

    def do_all(self, arg):
        """
        Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        arg_len = parse(arg)
        if len(arg_len) > 0 and arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_len = []
            for obj in storage.all().values():
                if len(arg_len) > 0 and arg_len[0] == obj.__class__.__name__:
                    obj_len.append(obj.__str__())
                elif len(arg_len) == 0:
                    obj_len.append(obj.__str__())
            print(obj_len)

    def do_count(self, arg):
        """
        Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
        """
        arg_len = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_len[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        arg_len = parse(arg)
        obj_dict = storage.all()

        if len(arg_len) == 0:
            print("** class name missing **")
            return False
        if arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_len) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_len[0], arg_len[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_len) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_len) == 3:
            try:
                type(eval(arg_len[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_len) == 4:
            obj = obj_dict["{}.{}".format(arg_len[0], arg_len[1])]
            if arg_len[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[arg_len[2]])
                obj.__dict__[arg_len[2]] = val_type(arg_len[3])
            else:
                obj.__dict__[arg_len[2]] = arg_len[3]
        elif type(eval(arg_len[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_len[0], arg_len[1])]
            for k, v in eval(arg_len[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = val_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


def parse(arg):
    regex_curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if regex_curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:regex_curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(regex_curly_braces.group())
        return retl


if __name__ == "__main__":
    HBNBCommand().cmdloop()