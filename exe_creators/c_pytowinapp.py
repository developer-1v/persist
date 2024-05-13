from print_tricks import pt
pt.easy_imports('main.py')
from imports_file import *

import os
import subprocess

class PytowinappCreator(ExeCreator):
    
    def __init__(self, source_path, main_file):
        super().__init__(source_path, "pytowinapp")
        self.main_file = main_file

    def generate_requirements(self):
        # Ensure the directory exists
        if not os.path.exists(self.source_path):
            os.makedirs(self.source_path)
        
        # Run pipreqs to generate requirements.txt
        subprocess.run(['pipreqs', self.source_path, '--force'], check=True)
        # subprocess.run(['preq', self.source_path], check=True)

    def create_exe(self, show_console=False):
        from py_to_win_app import Project

        try:
            self.generate_requirements()
            dir = os.path.join(os.getcwd(), self.source_path)
            pt(dir)

            project = Project(
                input_dir=dir,  # Use the current directory
                main_file=self.main_file
            )

            project.build(python_version="3.11.0", show_console=show_console)
            project.make_dist()
            
        finally:
                ...
        #     # Change back to the original directory
        #     os.chdir(original_dir)
        
if __name__ == "__main__":
    pytowinapp_creator = PytowinappCreator("test_source_dir", "test_source_file.py")
    
    pt.t()
    pytowinapp_creator.create_exe(show_console=True)
    pt.t()

