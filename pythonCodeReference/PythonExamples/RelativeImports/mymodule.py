from libs import mylib

print("mymodule.py:", __name__)

def divide():
    pass

# # -- can't do relative imports from top-level file --

# from .libs import mylib

# # -- parent imports --

# import libs.operations.operator
