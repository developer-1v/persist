print('1')
from imports_file import *
print('2')
# from print_tricks import pt
# pt.easy_testing(__name__)
# pt.easy_imports('main.py')

# from c_cx_freeze import CxFreezeCreator
# from c_cython_py2exe import CythonPy2ExeCreator
# from c_cython_pyvan import CythonPyVanCreator
# from c_cython_compiler import CythonCompilerCreator
# from c_cython_bat import CythonBatCreator
# from c_py2exe import Py2ExeCreator
# from c_pyvan import PyVanCreator



import sys

def main():
    script_name = 'test.py'
    
    # Simulate detailed command line arguments
    # Example: ['main.py', 'build', '--target', 'script_name']
    # You need to adjust these arguments based on the actual expected format.
    sys.argv = ['main.py', 'build', '--target', script_name]
    pt(sys.argv)
    execution_mode = 'ask'  # Options: 'ask', 'continue'
    
    creators = [
        CythonCompilerCreator(script_name, "cython_compiler"),
    ]
    
    for creator in creators:
        result = creator(script_name)
        if result:
            print("Executable creation succeeded.")
            find_and_create_shortcut(script_name, creator)

            if execution_mode == 'ask':
                response = input("Continue with the next method? (y/n): ")
                if response.lower() != 'y':
                    break
        else:
            print("Executable creation failed.")
            if execution_mode == 'ask':
                response = input("Attempt the next method? (y/n): ")
                if response.lower() != 'y':
                    break
        if execution_mode == 'continue':
            continue

if __name__ == "__main__":
    main()