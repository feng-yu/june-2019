import os
from contextlib import contextmanager

"""
Demo the context manager with function
"""
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


"""
Demo the context manager with class
"""
class Open_File():
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, *args):
        self.file.close()

"""
Test the context manager with function
"""
print(f'current directory: %s' % os.getcwd())
with change_dir('c:/'):
    print()
    print(os.listdir())
    print()
print(f'current directory: %s' % os.getcwd())


"""
Test the context manager with class
"""
with Open_File('test.txt', 'w') as f:
    f.write('Testing')

print(f.closed)