from imports_file import *

class CythonCompilerCreator(ExeCreator):
    def create_exe(self):
        try:
            subprocess.check_call([sys.executable, "-m", "cython_compiler", "script.py", "--output_dir", self.output_dir])
            print("EXE created with cython-compiler.")
            return True
        except Exception as e:
            print(f"Failed with cython-compiler: {e}")
            return False

