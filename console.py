#!/usr/bin/env python3
"""
Here goes the documentation for the console module
"""
from models.base_model import BaseModel
import cmd, sys
#from bye import quit

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None


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
        data = sys.argv[0]
        new_inst = BaseModel()
        print(BaseModel.id)
    
    def show(self):
        """ Prints the string representation of 
        an instance based on the class name 
        and id. Ex: $ show BaseModel 1234-1234-1234"""
    
    def destroy(self):
        """
         Deletes an instance based on the class name 
         and id (save the change into 
         the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
    
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
