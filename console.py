#!/usr/bin/python3
"""
Module for the HBNB command interpreter
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    valid_classes = [
            "BaseModel",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review",
            "User"
            ]

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a specified class"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return

        print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return

        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_objs = storage.all()

        if not args:
            print([str(obj) for obj in all_objs.values()])
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        print([
            str(obj) for key, obj in all_objs.items()
            if key.startswith(class_name)
            ])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        all_objs = storage.all()
        if key not in all_objs:
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
        instance = all_objs[key]
        try:
            attribute_value = eval(attribute_value)
        except (SyntaxError, ValueError):
            pass

        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def precmd(self, line):
        """Handle show() and destroy() commands"""
        if '.show(' in line and line.endswith(')'):
            class_and_id = line.split('(')[1][:-1]
            class_name, instance_id = class_and_id.split('.')
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return ""
            key = "{}.{}".format(class_name, instance_id)
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return ""
            print(all_objs[key])
            return ""
        elif '.destroy(' in line and line.endswith(')'):
            class_and_id = line.split('(')[1][:-1]
            class_name, instance_id = class_and_id.split('.')
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return ""
            key = "{}.{}".format(class_name, instance_id)
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return ""
            del all_objs[key]
            storage.save()
            return ""
        return line

    def precmd(self, line):
        """Handle update() command"""
        if '.update(' in line and line.endswith(')'):
            class_id_and_dict = line.split('(')[1][:-1]
            class_name, instance_id_and_dict = class_id_and_dict.split('.')
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return ""
            instance_id, update_dict_str = instance_id_and_dict.split(',', 1)
            key = "{}.{}".format(class_name, instance_id)
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return ""
            try:
                update_dict = eval(update_dict_str)
            except (SyntaxError, ValueError):
                print("** invalid dictionary representation **")
                return ""
            if not isinstance(update_dict, dict):
                print("** invalid dictionary representation **")
                return ""
            instance = all_objs[key]
            for k, v in update_dict.items():
                try:
                    v = eval(v)
                except (SyntaxError, ValueError):
                    pass
                setattr(instance, k.strip(), v)
            instance.save()
            return ""
        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
