#!/usr/bin/python3
""" Module for the entry point of thr command interpreter """

import cmd
<<<<<<< HEAD
from models import storage
from models.engine import storage
=======
from models.base_model import BaseModel
from models import storage
>>>>>>> test_branch
import re
import json


class HBNBCommand(cmd.Cmd):
    """ Class for the command interpreter """

    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches"""
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class syntax"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_for_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_for_uid_and_args:
            uid = match_for_uid_and_args.group(1)
            attr_or_dict = match_for_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_for_dict = re.search('^{.*})$', attr_or_dict)
            if match_for_dict:
                self.update_dict(classname, uid, match_for_dict.group(1))
                return ""
            match_for_attr_and_value = re.search('^(?:"([^"]*)")?(?:, (.*))?$\
                    ', attr_or_dict)
            if match_for_attr_and_value:
                attr_and_value = (match_for_attr_and_value.group(1) or "") +\
                    " " + (match_for_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """ Helper method for update func with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
<<<<<<< HEAD
        elif className not in storage.classes():
=======
        elif classname not in storage.classes():
>>>>>>> test_branch
            print("** class does not exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
<<<<<<< HEAD
            key = "{}.{}".format(className, uid)
            if key not in Storage.all():
                print("** no instance found **")
            else:
                attributes = _storage.attribites()[className]
=======
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attribites()[className]
>>>>>>> test_branch
                for attributes, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """Handles End Of File character"""
        print()
        return True

    def do_quit(self, line):
        """Exits program"""
        return True

    def emptyline(self):
        """Does nothing"""
        pass

    def do_create(self, line):
        """Creates an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class does not exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Print string representation of instance """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Print all string representation of all instances"""
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """Counts the instances of a class"""
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """ Updates an instance by adding or updating attribute"""
        if line == "" or line is None:
            print("** class name missing **")
            return
        rex = r'^(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        className = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif className not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(className, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[className]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
