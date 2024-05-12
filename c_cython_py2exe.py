from imports_file import *

class CythonPy2ExeCreator(ExeCreator):
    def create_exe(self):
        
        try:
            subprocess.check_call([sys.executable, "-m", "cython", "script.py", "-o", os.path.join(self.output_dir, "script.c")])
            subprocess.check_call(["gcc", "-shared", "-pthread", "-fPIC", "-fwrapv", "-O2", "-Wall", "-fno-strict-aliasing", "-I/usr/include/python3.8", "-o", os.path.join(self.output_dir, "script.so"), os.path.join(self.output_dir, "script.c")])
            subprocess.check_call([sys.executable, "-m", "py2exe.build_exe", "script.py", "--dist-dir", self.output_dir])
            print("EXE created with Cython and py2exe.")
            return True
        except Exception as e:
            print(f"Failed with Cython and py2exe: {e}")
            return False
