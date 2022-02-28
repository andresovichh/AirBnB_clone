#!/usr/bin/env python3

import cmd, sys
from bye import quit

class HbnbShell(cmd.Cmd):
    prompt = '(hbnb) '
    file = None


    def do_quit(self, arg):
        'Stop recording, close the turtle window and exit: BYE'
        print('Thank you for using hbnb')
        quit(self)
    def do_EOF(self):
        """ EOF to exit"""
        quit()
    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    HbnbShell().cmdloop()