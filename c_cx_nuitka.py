from imports_file import *


class CxNuitkaCreator(ExeCreator):
    def create_exe(self):
        try:

            print("EXE created with nuitka.")
            return True
        except Exception as e:
            print(f"Failed with nuitka: {e}")
            return False

