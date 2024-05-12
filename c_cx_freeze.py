

from imports_file import *

class CxFreezeCreator(ExeCreator):
    def create_exe(self):
        from cx_Freeze import setup, Executable
        setup(
            name="YourApp",
            version="0.1",
            description="Your app description",
            executables=[Executable("script.py")],
            options={"build_exe": {"build_exe": self.output_dir}}
        )
        subprocess.check_call([sys.executable, "setup.py", "build"])

if __name__ == "__main__":
    CxFreezeCreator("test.py", "cxfreeze").create_exe()