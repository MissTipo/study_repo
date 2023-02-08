#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import classes
import models
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is the class definition for the command interpreter"""
    prompt = "(hbnb) "
    #classes = {'basemodel':BaseModel}
    #classes = ["BaseModel"]

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

    # def emptyline(self):
        """Does nothing"""
        # pass

    def do_create(self, line):
        """Creates an instance"""
        args = shlex.split(line)
        if len(args) == 0:
            print("Class name missing!")
            return False
        if args[0] not in classes:
            print("class does not exist!")
            return False
        instance = classes[args[0]]()
        print (instance.id)
        instance.save()

    def do_show(self, line):
        """show instance of class and uuid"""
        args = shlex.split(line)
        if len(args) == 0:
            print("Class name missing")
            return False
        if args[0] not in classes:
            print("class does not exist!")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        model = args[0] + "." + args[1]
        models.storage.all()
        if model not in models.storage.all():
            print("** no instance found **")
            return False
        print(models.storage.all()[model])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(line)
        if len(args) == 0:
            print('** class name missing **')
            return False
        if args[0] not in classes:
            print("** class doesn't exist  **")
            return False
        if len(args) == 1:
            print('** instance id missing **')
            return False
        model = args[0] + "." + args[1]
        models.storage.all()
        if model not in models.storage.all():
            print('** no instance found **')
            return False
        else:
            del models.storage.all()[model]

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        if line not in classes:
            print("** class doesn't exist **")
        else:
            cls = models.storage.all()
            for value in cls.values():
                print(value)

    def do_update(self, line):
        args = shlex.split(line)
        if len(args) == 0:
            print('** class name missing **')
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print('** instance id missing **')
            return False
        key = args[0] + "." + args[1]
        model = models.storage.all()
        if key not in model:
            print('** no instance found **')
            return False
        if len (args) == 2:
            print('** attribute name missing **')
        if len(args) == 3:
            print('** value missing **')

        if len(args) >= 4 and key in model.keys():
            new_attribute = model[key].to_dict()
            attribute_key = args[2]
            attribute_value = args[3]
            new_attribute[attribute_key] = attribute_value
            new_cls_obj = BaseModel(**new_attribute)
            new_cls_obj.save()
            storage.new(new_cls_obj)





if __name__ == '__main__':
    HBNBCommand().cmdloop()
