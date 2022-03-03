#!/usr/bin/env python3
"""
Here goes the documentation for the console module
"""
from models.base_model import BaseModel
import cmd
import sys
import readline
from models import storage
from models.engine.file_storage import FileStorage
import json
# from bye import quit


class HBNBCommand(cmd.Cmd):
    """ This is the HBNB command line interpreter
    definiion"""

    prompt = '(hbnb) '
    file = None

    all_classes = {"BaseModel": BaseModel, "something": FileStorage}
    attributes = ["updated_at", "created_at", "id"]
    specs = ["\'", "\""]

    def do_quit(self, args):
        'Quit command to exit the program'
        print('Thank you for using hbnb')
        quit()

    def do_EOF(self, args):
        """ EOF to exit"""
        quit()

    def close(self):
        """ close method definition"""
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        """
        emptyline do nothing
        """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
        saves it to the json file and prints the id
        Ex. $ create BaseModel"""
        # command = arg.split()
        # name = command[0]
        # 1. Check if class name was passed to create foo
        if not arg:
            print("** class name missing **")
        else:
            # 2. spit the args
            command = arg.split()
            name = command[0]
            if name not in self.all_classes:
                # 3. Check if the given class is a
                # real one
                print("** class doesn't exist **")
            else:
                # 4. if class is real, do as asked.
                # create new instance, print it's id
                # and save it
                new_inst = self.all_classes[name]()
                print(new_inst.id)
                new_inst.save()

    def do_show(self, arg):
        """ Prints the string representation of
        an instance based on the class name
        and id. Ex: $ show BaseModel 1234-1234-1234"""
        if not arg:
            print("** class name missing **")

        else:
            command = arg.split()
            class_name = command[0]
            if class_name not in self.all_classes:
                print("** class doesn't exist **")
            elif len(command) == 1:
                print("** instance id missing **")
            else:
                find = command[0]+"."+command[1]
                if find not in storage.all():
                    print("** no instance found **")
                else:
                    objects = storage.all()
                    print(objects[find])

    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name
         and id (save the change into
         the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")

        else:
            command = arg.split()
            class_name = command[0]
            if class_name not in self.all_classes:
                print("** class doesn't exist **")
                return
            if len(command) < 2:
                print("** instance id missing **")
                return
            find = command[0]+"."+command[1]
            if find not in storage.all():
                print("** no instance found **")
                return
            else:
                objects = storage.all()
                del objects[find]
                # https://www.geeksforgeeks.org/python-del-to-delete-objects/
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        """
        if arg:
            command = arg.split()
            class_name = command[0]
            if command[0] not in self.all_classes:
                print("** class doesn't exist **")
            else:
                lst_w_classnme = []
                all_objects = storage.all()
                for k in all_objects:
                    cls_nme = k.split(".")
                    if cls_nme[0] == class_name:
                        lst_w_classnme.append(str(all_objects[k]))
                print(lst_w_classnme)

        if not arg:
            all_objects = storage.all()
            new_list = []

            for k in all_objects:
                new_list.append(str(all_objects[k]))
            print(new_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        command = arg.split()
        if not arg:
            print("** class name missing **")
        elif command[0] not in self.all_classes:
            print("** class doesn't exist **")
            return
        elif len(command) == 1:
            print("** instance id missing **")
            return
        elif command[0] + '.' + command[1] not in storage.all():
            print("** no instance found **")
            return
        elif len(command) == 2:
            print("** attribute name missing **")
            return
        elif len(command) == 3:
            print("** value missing **")
            return
        else:
            obj = storage.all()
            key = command[0] + '.' + command[1]

            if key in obj:
                if command[2] not in self.attributes:
                    if command[3][0] in self.specs \
                       and command[3][-1] in self.specs:
                        setattr(obj[key], command[2], str(command[3][1: -1]))
                    else:
                        setattr(obj[key], command[2], str(command[3]))
                    storage.save()
                else:
                    print("** no instance found **")
                    return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
