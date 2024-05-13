from imports_file import *

class CythonBatCreator(ExeCreator):
    def create_exe(self):
        try:
            with open(os.path.join(self.output_dir, "compile.bat"), "w") as bat:
                bat.write(f"cythonize -i {os.path.join(self.output_dir, 'script.py')}\n")
            subprocess.check_call([os.path.join(self.output_dir, "compile.bat")])
            print("EXE created with Cython using BAT file.")
            return True
        except Exception as e:
            print(f"Failed with Cython using BAT file: {e}")
            return False
        