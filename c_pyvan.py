from imports_file import *

class PyVanCreator(ExeCreator):
    def create_exe(self):
        try:
            subprocess.check_call([sys.executable, "-m", "pyvan", "--main_file", "script.py", "--output_dir", self.output_dir])
            print("EXE created with PyVan.")
            return True
        except Exception as e:
            print(f"Failed with PyVan: {e}")
            return False
