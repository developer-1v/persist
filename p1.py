import os
import subprocess
import sys

def create_exe_with_cxfreeze():
    try:
        from cx_Freeze import setup, Executable
        setup(
            name="YourApp",
            version="0.1",
            description="Your app description",
            executables=[Executable("script.py")]
        )
        subprocess.check_call([sys.executable, "setup.py", "build"])
        print("EXE created with cx_Freeze.")
        return True
    except Exception as e:
        print(f"Failed with cx_Freeze: {e}")
        return False

def create_exe_with_cython_py2exe():
    try:
        subprocess.check_call([sys.executable, "-m", "cython", "script.py", "-o", "script.c"])
        subprocess.check_call(["gcc", "-shared", "-pthread", "-fPIC", "-fwrapv", "-O2", "-Wall", "-fno-strict-aliasing", "-I/usr/include/python3.8", "-o", "script.so", "script.c"])
        subprocess.check_call([sys.executable, "-m", "py2exe.build_exe", "script.py"])
        print("EXE created with Cython and py2exe.")
        return True
    except Exception as e:
        print(f"Failed with Cython and py2exe: {e}")
        return False

def create_exe_with_cython_pyvan():
    try:
        subprocess.check_call([sys.executable, "-m", "cython", "script.py", "-o", "script.c"])
        subprocess.check_call(["gcc", "-shared", "-pthread", "-fPIC", "-fwrapv", "-O2", "-Wall", "-fno-strict-aliasing", "-I/usr/include/python3.8", "-o", "script.so", "script.c"])
        subprocess.check_call([sys.executable, "-m", "pyvan", "--main_file", "script.py"])
        print("EXE created with Cython and PyVan.")
        return True
    except Exception as e:
        print(f"Failed with Cython and PyVan: {e}")
        return False

def create_exe_with_cython_compiler():
    try:
        subprocess.check_call([sys.executable, "-m", "cython_compiler", "script.py"])
        print("EXE created with cython-compiler.")
        return True
    except Exception as e:
        print(f"Failed with cython-compiler: {e}")
        return False

def create_exe_with_py2exe():
    try:
        subprocess.check_call([sys.executable, "-m", "py2exe.build_exe", "script.py"])
        print("EXE created with py2exe.")
        return True
    except Exception as e:
        print(f"Failed with py2exe: {e}")
        return False

def create_exe_with_pyvan():
    try:
        subprocess.check_call([sys.executable, "-m", "pyvan", "--main_file", "script.py"])
        print("EXE created with PyVan.")
        return True
    except Exception as e:
        print(f"Failed with PyVan: {e}")
        return False

def create_exe_with_cython_bat():
    try:
        with open("compile.bat", "w") as bat:
            bat.write("cythonize -i script.py\n")
        subprocess.check_call(["compile.bat"])
        print("EXE created with Cython using BAT file.")
        return True
    except Exception as e:
        print(f"Failed with Cython using BAT file: {e}")
        return False

def main():
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
        if creator():
            print("Executable creation succeeded.")
            break
    else:
        print("All methods failed to create an executable.")

if __name__ == "__main__":
    main()