#!/usr/bin/env python3
"""
Here goes the documentation for the console module
"""

import cmd, sys
#from bye import quit

class HbnbShell(cmd.Cmd):
    prompt = '(hbnb) '
    file = None


    def do_quit(self, args):
        'Quit the console'
        print('Thank you for using hbnb')
        quit()
    def do_EOF(self, args):
        """ EOF to exit"""
        quit()
    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    HbnbShell().cmdloop()