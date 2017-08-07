from share_visitor import Visitor
import sys

def gdrive_command(*args):
    BASE_COMMAND='gdrive share update'
    return BASE_COMMAND + ' ' + ' '.join(args)

class ReadOnlyVisitor(Visitor):
    def visit_share(self, file_hash, file_name, share_hash, email, role):
        cmd = gdrive_command(file_hash, share_hash, 'reader')

def main():
    root = sys.argv[1]
    b = ReadOnlyVisitor(root)
    b.visit()

if __name__ == '__main__':
    main()
