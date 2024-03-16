#!/usr/bin/env python3
"""This module is a simple console for the user to interact with the program.
It uses the cmd module to create a simple command line interface that will be used for test harnessing.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """This class creates a simple command line interface for the user to interact with the program.
    It inherits from the cmd.Cmd class and overrides the default methods to create a custom command line interface.
    """
    intro = 'Welcome to the test harness. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exits the test harness."""
        print('Goodbye')
        return True

    # alias for the quit command
    do_EOF = do_quit

    # documetation for the help command
    def help_EOF(self):
        """Exits the test harness."""
        print('Exits the test harness.')

    # documentation for the help command
    def help_help(self):
        """List available commands with "help" or detailed help with "help cmd"."""
        print('List available commands with "help" or detailed help with "help cmd".')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
