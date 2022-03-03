#!/usr/bin/env python3
"""
Here goes the documentation for the console module
"""
from models.base_model import BaseModel
import cmd, sys
import readline
from models import storage
from models.engine.file_storage import FileStorage
#from bye import quit

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    all_classes = {"BaseModel": BaseModel, "something": FileStorage}


    def do_quit(self, args):
        'Quit command to exit the program'
        print('Thank you for using hbnb')
        quit()

    def do_EOF(self, args):
        """ EOF to exit"""
        quit()

    def close(self):
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
            if len(command) < 2:
                print("** instance id missing **")
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
                objects[find].remove()    
  



    
    def all(self):
        """
        Prints all string representation of all instances 
        based or not on the class name. Ex: $ all BaseModel or $ all
        """
    
    def update(self):
        """
        Updates an instance based on the class name and id 
        by adding or updating attribute (save the change into the JSON file). 
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
