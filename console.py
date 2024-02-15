#!/usr/bin/python3
"""
This module contains the HBNBCommand class, which is a simple command
interpreter for the AirBnB clone project.
"""

import ast
import cmd
import json
from models import storage
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.classes = FileStorage.CLASSES
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF is encountered
        """
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        for pair in args[1:]:
            key, value = pair.split('=')
            setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        """
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        try:
            class_name = args[0]
            if len(args) == 1:
                print('** instance id missing **')
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            print(storage.all().get(key, '** no instance found **'))
        except NameError:
            print('** class doesn\'t exist **')

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        try:
            class_name = args[0]
            if len(args) == 1:
                print('** instance id missing **')
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_objects = storage.all()
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print('** no instance found **')
        except NameError:
            print('** class doesn\'t exist **')


    def do_all(self, arg):
        """
        Prints all string representations of instances based on the class name.
        """
        try:
            if arg:
                class_name = arg.split()[0]
                print([str(obj) for obj in storage.all().values() if class_name == obj.__class__.__name__])
            else:
                print([str(obj) for obj in storage.all().values()])
        except NameError:
            print('** class doesn\'t exist **')

    def default(self, line):
        parts = line.split('.')
        if len(parts) == 2 and parts[1] == 'all()':
            class_name = parts[0]
            try:
                cls = eval(class_name)
                print([str(obj) for obj in storage.all().values() if isinstance(obj, cls)])
            except NameError:
                print('** class doesn\'t exist **')
        else:
            print('*** Unknown syntax: {}'.format(line))

    def default(self, line):
        """
        Default method to handle <class name>.count() syntax.
        """
        parts = line.split('.')
        if len(parts) == 2 and parts[1] == 'count()':
            class_name = parts[0]
            if class_name not in self.classes:
                print('** class doesn\'t exist **')
                return
            count = sum(1 for obj in storage.all().values() if isinstance(obj, self.classes[class_name]))
            print(count)
        else:
            print('*** Unknown syntax:', line)

    def default(self, line):
        """
        Default method to handle <class name>.<command>(<args>) syntax.
        """
        parts = line.split('(')
        if len(parts) == 2:
            class_command = parts[0].split('.')
            if len(class_command) == 2:
                class_name, command = class_command
                args = parts[1][:-1]  # Remove the trailing ')'
                if class_name not in self.classes:
                    print('** class doesn\'t exist **')
                    return
                class_obj = self.classes[class_name]
                if command == 'show':
                    self.do_show(f"{class_name} {args}")
                elif hasattr(class_obj, command):
                    method = getattr(class_obj, command)
                    method(self, args)
                else:
                    print('** command doesn\'t exist **')
            else:
                print('*** Unknown syntax:', line)
        else:
            print('*** Unknown syntax:', line)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print('** class name missing **')
            return

        try:
            class_name = args[0]
            if len(args) < 2:
                print('** instance id missing **')
                return

            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_objects = models.storage.all()

            if key not in all_objects:
                print('** no instance found **')
                return

            instance = all_objects[key]

            if len(args) < 3:
                print('** attribute name missing **')
                return

            attribute_name = args[2]
            if len(args) < 4:
                print('** value missing **')
                return

            attribute_value = args[3]
            
            # Update the attribute of the instance
            setattr(instance, attribute_name, attribute_value)
            instance.save()

        except Exception as e:
            print(e)





if __name__ == '__main__':
    HBNBCommand().cmdloop()