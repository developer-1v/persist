import os
import subprocess
import sys



def get_output_directory(script_filename, function_name, attempt_number):
    return os.path.join("projects", f"{script_filename}_{attempt_number}_{function_name}")

def create_exe_with_cxfreeze(script_filename, attempt_number=1):
    output_dir = get_output_directory(script_filename, "cxfreeze", attempt_number)
    os.makedirs(output_dir, exist_ok=True)
    try:
        from cx_Freeze import setup, Executable
        setup(
            name="YourApp",
            version="0.1",
            description="Your app description",
            executables=[Executable("script.py")],
            options={"build_exe": {"build_exe": output_dir}}
        )
        subprocess.check_call([sys.executable, "setup.py", "build"])
        print("EXE created with cx_Freeze.")
        return True
    except Exception as e:
        print(f"Failed with cx_Freeze: {e}")
        return False

def create_exe_with_cython_py2exe(script_filename, attempt_number=1):
    output_dir = get_output_directory(script_filename, "cython_py2exe", attempt_number)
    os.makedirs(output_dir, exist_ok=True)
    try:
        subprocess.check_call([sys.executable, "-m", "cython", "script.py", "-o", os.path.join(output_dir, "script.c")])
        subprocess.check_call(["gcc", "-shared", "-pthread", "-fPIC", "-fwrapv", "-O2", "-Wall", "-fno-strict-aliasing", "-I/usr/include/python3.8", "-o", os.path.join(output_dir, "script.so"), os.path.join(output_dir, "script.c")])
        subprocess.check_call([sys.executable, "-m", "py2exe.build_exe", "script.py", "--dist-dir", output_dir])
        print("EXE created with Cython and py2exe.")
        return True
    except Exception as e:
        print(f"Failed with Cython and py2exe: {e}")
        return False

def create_exe_with_cython_pyvan(script_filename, attempt_number=1):
    output_dir = get_output_directory(script_filename, "cython_pyvan", attempt_number)
    os.makedirs(output_dir, exist_ok=True)
    try:
        subprocess.check_call([sys.executable, "-m", "cython", "script.py", "-o", os.path.join(output_dir, "script.c")])
        subprocess.check_call(["gcc", "-shared", "-pthread", "-fPIC", "-fwrapv", "-O2", "-Wall", "-fno-strict-aliasing", "-I/usr/include/python3.8", "-o", os.path.join(output_dir, "script.so"), os.path.join(output_dir, "script.c")])
        subprocess.check_call([sys.executable, "-m", "pyvan", "--main_file", "script.py", "--output_dir", output_dir])
        print("EXE created with Cython and PyVan.")
        return True
    except Exception as e:
        print(f"Failed with Cython and PyVan: {e}")
        return False

def create_exe_with_cython_compiler(script_filename, attempt_number=1):
    output_dir = get_output_directory(script_filename, "cython_compiler", attempt_number)
    os.makedirs(output_dir, exist_ok=True)
    try:
        subprocess.check_call([sys.executable, "-m", "cython_compiler", "script.py", "--output_dir", output_dir])
        print("EXE created with cython-compiler.")
        return True
    except Exception as e:
        print(f"Failed with cython-compiler: {e}")
        return False

def create_exe_with_py2exe(script_filename, attempt_number=1):
    output_dir = get_output_directory(script_filename, "py2exe", attempt_number)
    os.makedirs(output_dir, exist_ok=True)
    try:
        subprocess.check_call([sys.executable, "-m", "py2exe.build_exe", "script.py", "--dist-dir", output_dir])
        print("EXE created with py2exe.")
        return True
    except Exception as e:
        print(f"Failed with py2exe: {e}")
        return False

def create_exe_with_pyvan(script_filename, attempt_number=1):
    output_dir = get_output_directory(script_filename, "pyvan", attempt_number)
    os.makedirs(output_dir, exist_ok=True)
    try:
        subprocess.check_call([sys.executable, "-m", "pyvan", "--main_file", "script.py", "--output_dir", output_dir])
        print("EXE created with PyVan.")
        return True
    except Exception as e:
        print(f"Failed with PyVan: {e}")
        return False

def create_exe_with_cython_bat(script_filename, attempt_number=1):
    output_dir = get_output_directory(script_filename, "cython_bat", attempt_number)
    os.makedirs(output_dir, exist_ok=True)
    try:
        with open(os.path.join(output_dir, "compile.bat"), "w") as bat:
            bat.write(f"cythonize -i {os.path.join(output_dir, 'script.py')}\n")
        subprocess.check_call([os.path.join(output_dir, "compile.bat")])
        print("EXE created with Cython using BAT file.")
        return True
    except Exception as e:
        print(f"Failed with Cython using BAT file: {e}")
        return False

def main():
    # Set this variable to 'ask' to decide after each attempt, or 'continue' to try all methods regardless
    execution_mode = 'ask'  # Options: 'ask', 'continue'
    
    creators = [
        create_exe_with_cxfreeze,
        create_exe_with_cython_py2exe,
        create_exe_with_cython_pyvan,
        create_exe_with_cython_compiler,
        create_exe_with_py2exe,
        create_exe_with_pyvan,
        create_exe_with_cython_bat
    ]
    
    for creator in creators:
        result = creator('test.py')
        if result:
            print("Executable creation succeeded.")
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