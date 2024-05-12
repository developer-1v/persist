from imports_file import *

class Py2ExeCreator(ExeCreator):
    def create_exe(self):
        try:
            subprocess.check_call([sys.executable, "-m", "py2exe.build_exe", "script.py", "--dist-dir", self.output_dir])
            print("EXE created with py2exe.")
            return True
        except Exception as e:
            print(f"Failed with py2exe: {e}")
            return False
        