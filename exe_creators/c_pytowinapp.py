from print_tricks import pt
pt.easy_imports('main.py')
# import anyimport
# anyimport.init()

from imports_file import *

import os
import subprocess

class PytowinappCreator(ExeCreator):
    
    def __init__(self, source_path, main_file):
        super().__init__(source_path, "pytowinapp")
        self.main_file = main_file

    def create_exe(self, show_console=True):
        
        try: 
            self.generate_requirements()
            ...
        except Exception as e:
            pt.e()
            pt.ex()

        dir, original_dir = self.setup_directories()
        try:
            self.create_show_console_script(dir)
            self.build_project(dir, show_console)
        finally:
            os.chdir(original_dir)


    def build_project(self, dir, show_console):
        from py_to_win_app import Project

        project = Project(
            input_dir=dir,
            main_file='_show_console_output.py'
        )
        project.build(python_version="3.11.0", show_console=show_console)
        project.make_dist()

if __name__ == "__main__":
    pytowinapp_creator = PytowinappCreator(
        "test_source_dir", "test_source_file.py"
        # "C:\.PythonProjects\smak", "smak.py"
        
        )
    pt.t()
    pytowinapp_creator.create_exe(show_console=True)
    pt.t()


'''
            ## Change the current working directory to the source path
            ## this is to prevent pytowinapp from creating build/dist
            ## in the persist directory, instead of the user's 
            ## source directory. 
            # 
            # 
            # '''