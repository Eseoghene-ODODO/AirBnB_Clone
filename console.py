#!/usr/bin/python3
"""
creating a command line for my AirBnB project
"""

import cmd
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand body"""
    into = print("Welcome to my AirBnB console.")
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit the command line to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the command line on EOF"""
        return True
    
    def do_help(self, arg):
        """Displays help message"""
        super().do_help(arg)

    def emptyline(self):
        """Does nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves to a JSON file"""
        if not arg:
            print("** class name missing  **")
        else:
            try:
                class_name = arg.split()[0]
                new_instance = globals()[class_name]()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on cls, id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        class_name = args[0]
        
        try:
            model_class = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing ** ")
        instance_id = args[1]
        storage = FileStorage()
        instances = storage._FileStorage__objects
        key = f"{class_name}.{instance_id}"
        instance = instances.get(key)
        if instance:
            print(str(instance))
        else:
            print("** no instance found **")
        if class_name == 'User':
            self.do_show(f"User {instance_id}")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            model_class = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
        instance_id = args[1]
        storage = FileStorage()
        instances = storage._FileStorage__objects
        key = f"{class_name}.{instance_id}"
        instance = instances.get(key)
        if instance:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")
        if class_name == 'User':
            self.do_destroy(f"User {instance_id}")

    def do_all(self, arg):
        """Prints all string representation of all the based or not on the
        class name"""
        args = arg.split()
        class_name = args[0] if args else None
        if class_name and not hasattr(storage, class_name):
            print("** class doesn't exist **")
            return
        instances = storage.all()
        if class_name:
            instances = {
                    key: obj for key, obj in instances.items()
                    if isinstance(obj, getattr(storage, class_name))
                    }
        print([str(obj) for obj in instances.values()])
        if class_name == 'User':
            self.do_all("User")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exit **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        storage = FileStorage()
        instances = storage._FileStorage__objects
        key = f"{class_name}.{instance_id}"
        instance = None
        for obj in instances.values():
            if obj.__class__.__name__ == class_name and obj.id == instance_id:
                instance = obj
                break
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        try:
            setattr(
                    instance,
                    attribute_name,
                    type(
                        getattr(
                            instance,
                            attribute_name
                            )
                        )
                    (
                        attribute_value
                        )
                    )
        except AttributeError:
            print("** attribute name doesn't exist **")
        if class_name == 'User':
            self.do_update(
                    f"User {instance_id} {attribute_name} {attribute_value}"
                    )
        storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
