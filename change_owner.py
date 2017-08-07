from share_visitor import Visitor
import os
import sys

def gdrive_command(*args):
    BASE_COMMAND='gdrive share'
    return BASE_COMMAND + ' ' + ' '.join(args)

class ChangeOwnerVisitor(Visitor):
    def visit_file(self, file_hash, file_name):
        cmd = gdrive_command('--email %s'%self.email,'--type user','--role owner')
        os.system(cmd)

def main():
    root = sys.argv[2]
    new_owner = sys.argv[1]
    b = ChangeOwnerVisitor(root)
    b.email = new_owner
    b.visit()

if __name__ == '__main__':
    main()
