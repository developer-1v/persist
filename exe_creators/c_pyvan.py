from print_tricks import pt
pt.easy_imports('main.py')
from imports_file import *

class PyVanCreator(ExeCreator):
    
    def __init__(self, 
                source_path, 
                main_file, 
                show_console=False, 
                keep_console_open=False,
                use_existing_requirements=False,
                pyvan_generate_pipreqs=True
                ):
        super().__init__(source_path, "pyvan")
        
        self.main_file = main_file
        
        self.show_console = show_console
        self.keep_console_open = keep_console_open
        self.use_existing_requirements = use_existing_requirements
        self.pyvan_generate_pipreqs = pyvan_generate_pipreqs

    def create_exe(self):
        if not self.use_existing_requirements:
            try: 
                self.generate_requirements()
                self.pyvan_generate_pipreqs = False
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
        import pyvan

        main_file_name = self.main_file if not self.keep_console_open else "_show_console_output.py"

        OPTIONS = {
            "main_file_name": main_file_name,
            "show_console": self.show_console,
            "use_existing_requirements": self.use_existing_requirements,
            "use_pipreqs": self.pyvan_generate_pipreqs,
            "build_dir": "dist",
            "pydist_sub_dir": "pydist",
            "source_sub_dir": "",
            "verbose": True,
            # "include_modules": ["tkinter"]
        }

        pyvan.build(**OPTIONS)

if __name__ == "__main__":
    pyvan_creator = PyVanCreator(
        "test_source_dir", "test_source_file.py",
        use_existing_requirements=True,
        pyvan_generate_pipreqs=False,
        show_console=True, keep_console_open=True
    )
    pt.t()
    pyvan_creator.create_exe()
    pt.t()

