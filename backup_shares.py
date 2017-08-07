from share_visitor import Visitor
import sys

class BackupVisitor(Visitor):
    def visit_start(self):
        self.ofile = open(self.output_file, 'w', 0)

    def visit_share(self, file_hash, file_name, share_hash, email, role):
        str = ','.join([file_hash, file_name, share_hash, email, role]) + '\n'
        self.ofile.write(str)

def main():
    root = sys.argv[2]
    b = BackupVisitor(root)
    b.output_file = sys.argv[1]
    b.visit()

if __name__ == '__main__':
    main()
