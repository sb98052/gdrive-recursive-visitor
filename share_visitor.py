import sys
import pdb
import os
import re
import time

def gdrive_command(*args):
    BASE_COMMAND='gdrive --no-header --separator ,'
    return BASE_COMMAND + ' ' + ' '.join(args)

class Visitor:
    def __init__(self, root):
        self.root = root

    def visit_share(self, file_hash, file_name, share_hash, email, role):
        pass
    
    def visit_file(self, file_hash, file_name):
        pass

    def visit_start(self):
        pass

    def visit_end(self):
        pass

    def visit(self):
        queue = [('dir',self.root)]

        try:
            self.visit_start()
        except AttributeError:
            pass

        while queue:
            t, f = queue.pop()

            # Get file name
            cmd = gdrive_command('info', f)
            name_str = os.popen(cmd).read()
            matches = re.search(r'Name: (.*)', name_str, re.MULTILINE)

            while True:
                try:
                    name = matches.group(1)
                except AttributeError:
                    print "Error connecting... sleeping."
                    time.sleep(5)
                
            try:
                self.visit_file(f, name)
            except AttributeError:
                pass

            # Get share list
            cmd = gdrive_command('share list', f)
            shares = os.popen(cmd).read().splitlines()

            for share in shares:
                items = share.split(',')

                try:
                    self.visit_share(f, name, items[0], items[3], items[2])
                except AttributeError:
                    pass

            if t == 'dir':
                cmd = gdrive_command('list -q', '\'"%s" in parents\''%f)
                sub = os.popen(cmd).read().splitlines()

                for s in sub:
                    spl = s.split(',')
                    fid = spl[0]
                    ftype = spl[2]

                    queue.append((ftype, fid))
