from imports_file import *







def main():
    script_name = 'test.py'
    
    # CxFreezeCreator(script_name, "cxfreeze")
    # pytowinappCreator(script_name, "pyinstaller")
    # pt.ex()

    execution_mode = 'ask'  # Options: 'ask', 'continue'
    
    creators = [
        # CxFreezeCreator(script_name, "cxfreeze"),
        # CythonPytowinappCreator(script_name, "cython_pytowinapp"),
        # CythonPyVanCreator(script_name, "cython_pyvan"),
        # CythonCompilerCreator(script_name, "cython_compiler"),
        # CythonBatCreator(script_name, "cython_bat"),
        PytowinappCreator(script_name, "pytowinapp"),
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
    
    
    
'''
Error's: 
    very possibly are within the ExeCreator class. 
    
    Also, instantiating these creators doesn't do anything .We need to 
    create_exe() method. 
    
    '''