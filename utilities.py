from imports_file import *

__all__ = [
    'ExeCreator', 
    'get_next_attempt_number', 
    'get_output_directory', 
    'create_shortcut', 
    'find_and_create_shortcut'
    ]

def get_next_attempt_number(script_name):
    # Get the absolute path of the directory this script is in
    dir_path = os.path.dirname(os.path.abspath(__file__))
    # The base path should point to the parent directory containing all script attempts
    base_path = os.path.join(dir_path, "projects")
    max_attempt = 0
    # Check if the base directory exists
    if os.path.exists(base_path):
        # List all folders in the base directory
        for folder in os.listdir(base_path):
            # Match folders that follow the pattern "script_name_attemptnumber"
            match = re.match(rf"{re.escape(script_name)}_(\d+)", folder)
            if match:
                attempt_num = int(match.group(1))
                if attempt_num > max_attempt:
                    max_attempt = attempt_num
    # Return the next attempt number
    return max_attempt + 1

def get_output_directory(script_name, function_name):
    attempt_number = get_next_attempt_number(script_name)
    script_folder = os.path.join("projects", f"{script_name}_{attempt_number}")
    function_folder = os.path.join(script_folder, function_name)
    os.makedirs(function_folder, exist_ok=True)
    return function_folder

def create_shortcut(exe_path, shortcut_dir):
    shortcut_path = os.path.join(shortcut_dir, 'LaunchApp.lnk')
    target = exe_path
    wDir = shortcut_dir
    icon = exe_path

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

def find_and_create_shortcut(script_name, function_name):
    output_dir = get_output_directory(script_name, function_name)
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".exe"):
                exe_path = os.path.join(root, file)
                create_shortcut(exe_path, os.path.dirname(output_dir))
                print(f"Shortcut created for {exe_path}")
                return


class ExeCreator:
    def __init__(self, script_filename, method_name):
        self.script_filename = script_filename
        self.method_name = method_name
        self.output_dir = self.get_output_directory()

    def get_output_directory(self):
        return get_output_directory(self.script_filename, self.method_name)

    def create_exe(self):
        raise NotImplementedError("Subclasses should implement this method")

    def execute(self):
        os.makedirs(self.output_dir, exist_ok=True)
        try:
            self.create_exe()
            print(f"EXE created with {self.method_name}.")
            return True
        except Exception as e:
            print(f"Failed with {self.method_name}: {e}")
            return False