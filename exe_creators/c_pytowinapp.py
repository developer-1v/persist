from print_tricks import pt
pt.easy_imports('main.py')
# import anyimport
# anyimport.init()

from imports_file import *

import os
import subprocess

class PytowinappCreator(ExeCreator):
    
    def __init__(self, 
            source_path, 
            main_file,
            show_console=False, 
            keep_console_open=False
            ):
        super().__init__(source_path, "pytowinapp")
        
        self.main_file = main_file
        
        self.show_console = show_console
        self.keep_console_open = keep_console_open

    def create_exe(self):
        
        try: 
            self.generate_requirements()
            ...
        except Exception as e:
            pt.e()
            pt.ex()

        dir, original_dir = self.setup_directories()
        try:
            self.create_show_console_script(dir)
            self.build_project(dir)
        finally:
            os.chdir(original_dir)


    def build_project(self, dir):
        from py_to_win_app import Project

        main_file_name = self.main_file if not self.keep_console_open else "_show_console_output.py"

        project = Project(
            input_dir=dir,
            main_file=main_file_name
        )
        project.build(python_version="3.11.0", show_console=self.show_console)
        project.make_dist()

if __name__ == "__main__":
    pytowinapp_creator = PytowinappCreator(
        "test_source_dir", "test_source_file.py",
        # "C:\.PythonProjects\smak", "smak.py"
        show_console=True, keep_console_open=True,
    )
    pt.t()
    pytowinapp_creator.create_exe()
    pt.t()


'''
            ## Change the current working directory to the source path
            ## this is to prevent pytowinapp from creating build/dist
            ## in the persist directory, instead of the user's 
            ## source directory. 
            # 
            # 
            # '''