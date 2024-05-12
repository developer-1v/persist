from imports_file import *

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




def main():
    script_name = 'test.py'
    
    CxFreezeCreator(script_name, "cxfreeze")
    pt.ex()

    execution_mode = 'ask'  # Options: 'ask', 'continue'
    
    creators = [
        CxFreezeCreator(script_name, "cxfreeze"),
        # CythonPy2ExeCreator(script_name, "cython_py2exe"),
        # CythonPyVanCreator(script_name, "cython_pyvan"),
        # CythonCompilerCreator(script_name, "cython_compiler"),
        # CythonBatCreator(script_name, "cython_bat"),
        # Py2ExeCreator(script_name, "py2exe"),
        # PyVanCreator(script_name, "pyvan"),
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