from print_tricks import pt
pt.easy_imports('main.py')
from imports_file import *

class PyVanCreator(ExeCreator):
    
    def __init__(self, source_path, main_file):
        super().__init__(source_path, "pyvan")
        self.main_file = main_file

    def create_exe(self, show_console=True):
        dir, original_dir = self.setup_directories()
        try:
            self.create_show_console_script(dir)
            self.build_project(dir, show_console)
        finally:
            os.chdir(original_dir)

    def build_project(self, dir, show_console):
        import pyvan

        OPTIONS = {
            "main_file_name": self.main_file,
            "show_console": show_console,
            "use_existing_requirements": False,
            "use_pipreqs": True,
            "build_dir": "dist",
            "pydist_sub_dir": "pydist",
            "source_sub_dir": "",
            "verbose": True
        }

        pyvan.build(**OPTIONS)

if __name__ == "__main__":
    pyvan_creator = PyVanCreator(
        "test_source_dir", "test_source_file.py"
    )
    pt.t()
    pyvan_creator.create_exe(show_console=True)
    pt.t()