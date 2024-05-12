# import argparse
from imports_file import *

class CxFreezeCreator:
    def __init__(self, script_filename, output_dir):
        self.script_filename = script_filename
        self.output_dir = output_dir

    def create_exe(self):
        from cx_Freeze import setup, Executable
        setup(
            name="YourApp",
            version="0.1",
            description="Your app description",
            executables=[Executable(self.script_filename)],
            options={"build_exe": {"build_exe": self.output_dir}}
        )
        # Assuming setup.py is correctly configured and present
        subprocess.check_call([sys.executable, "setup.py", "build"])

if __name__ == "__main__":
    script_filename = 'test.py'  # Directly specify the script path here
    output_dir = 'projects'  # Specify the output directory
    creator = CxFreezeCreator(script_filename, output_dir)
    creator.create_exe()

# import sys
# from cx_Freeze import setup, Executable

# # Define the build options
# build_exe_options = {
#     "packages": ["os"],  # Add any necessary packages
#     "excludes": ["tkinter"]  # Exclude unnecessary packages
# }

# # Define the base option
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"  # Use "Win32GUI" to hide the console window on Windows for GUI applications

# # Setup configuration
# setup(
#     name="YourApplication",
#     version="0.1",
#     description="Your Application Description",
#     options={"build_exe": build_exe_options},
#     executables=[Executable("test.py", base=base)]  # Replace 'script.py' with your script
# )

# # Running the build process
# sys.argv.append("build")  # Appends 'build' to the command line arguments
# if __name__ == "__main__":
#     setup()  # This will invoke the build process