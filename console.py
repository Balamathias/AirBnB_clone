#!/usr/bin/python3
"""Module for the AirBnB clone command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB clone."""

    intro = "Welcome to command interpreter for AirBnB clone. Type 'help' for commands. \n"
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit on EOF."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def help_quit(self):
        """Print help for quit command."""
        print("Quit the command interpreter.")

    def help_EOF(self):
        """Print help for EOF command."""
        print("Exit the program on EOF.")

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes and not isinstance(storage, FileStorage):
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)


    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                obj = objects[key]
                attr_name = args[2]
                attr_value = args[3]

                # Only update if attribute is not id, created_at, or updated_at
                if (
                    attr_name not in ['id', 'created_at', 'updated_at']
                    and hasattr(obj, attr_name)
                ):
                    # Cast the attribute value to the attribute type
                    attr_type = type(getattr(obj, attr_name))
                    setattr(obj, attr_name, attr_type(attr_value))
                    storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print string representation of all instances."""
        args = shlex.split(arg)
        objects = storage.all()

        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in storage.classes and not isinstance(storage, FileStorage):
            print("** class doesn't exist **")
        else:
            if isinstance(storage, FileStorage):
                # For FileStorage, directly access the dictionary of objects
                class_name = args[0]
                all_instances = {k: v for k, v in objects.items() if k.startswith(class_name)}
                print([str(obj) for obj in all_instances.values()])
            else:
                # For other storage implementations, use storage.classes
                print([str(obj) for key, obj in objects.items() if key.startswith(args[0])])


    def do_count(self, arg):
        """Count the number of instances of a class."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            all_instances = storage.all(class_name)
            count = len(all_instances)
            print(count)

    def do_destroy_id(self, arg):
        """Destroy an instance based on its ID."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            objects = storage.all()

            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update_id(self, arg):
        """Update an instance based on its ID."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            objects = storage.all()

            if key in objects:
                obj = objects[key]
                attr_name = args[2]
                attr_value = args[3]

                # Only update if attribute is not id, created_at, or updated_at
                if (
                    attr_name not in ['id', 'created_at', 'updated_at']
                    and hasattr(obj, attr_name)
                ):
                    # Cast the attribute value to the attribute type
                    attr_type = type(getattr(obj, attr_name))
                    setattr(obj, attr_name, attr_type(attr_value))
                    storage.save()
            else:
                print("** no instance found **")

    def do_update_dict(self, arg):
        """Update an instance based on its ID with a dictionary."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** dictionary representation missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            objects = storage.all()

            if key in objects:
                obj = objects[key]
                try:
                    dict_representation = eval(args[2])
                except Exception as e:
                    print("** invalid dictionary representation **")
                    return

                if isinstance(dict_representation, dict):
                    for key, value in dict_representation.items():
                        # Only update if attribute is not id, created_at, or updated_at
                        if (
                            key not in ['id', 'created_at', 'updated_at']
                            and hasattr(obj, key)
                        ):
                            # Cast the attribute value to the attribute type
                            attr_type = type(getattr(obj, key))
                            setattr(obj, key, attr_type(value))
                    storage.save()
                else:
                    print("** invalid dictionary representation **")
            else:
                print("** no instance found **")







if __name__ == '__main__':
    HBNBCommand().cmdloop()
