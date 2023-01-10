#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the class definition for the command interpreter"""
    prompt = "(hbnb) "


    def do_quit(self, line):
        """This command quits the command interpreter"""
        return True

    def help_quit(self):
        """This gives more information about the quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """This exits the program"""
        return True

    def help_EOF(self):
        """This gives more information about the quit command"""
        print("This is the end of file\n")

    def emptyline(self):
        """Does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
