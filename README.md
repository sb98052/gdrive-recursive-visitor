# Google Drive Recursive Visitor

This module lets you write scripts to recursively descend Google Drive files
and shares via a simple Python interface, and to operate upon them using the
[gdrive](https://github.com/sb98052/gdrive) command-line tool.

To install, run: `go get https://github.com/sb98052/gdrive`

*Note: You will need my forked version until my pull requests get merged into the original one*

## Example: Make a backup of current sharing permissions


```python
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
```

## Example: Change the owner of files recursively

```python
from share_visitor import Visitor
import os
import sys

def gdrive_command(*args):
    BASE_COMMAND='gdrive'
    return BASE_COMMAND + ' ' + ' '.join(args)

class ChangeOwnerVisitor(Visitor):
    def visit_file(self, file_hash, file_name):
        cmd = gdrive_command('share','--email %s'%self.email,'--type user','--role owner')
        os.system(cmd)

def main():
    root = sys.argv[2]
    new_owner = sys.argv[1]
    b = ChangeOwnerVisitor(root)
    b.email = new_owner
    b.visit()

if __name__ == '__main__':
    main()
```

## Example: Recursively change files to read-only

```python

```