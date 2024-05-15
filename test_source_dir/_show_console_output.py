import subprocess
import sys

if __name__ == '__main__':
    subprocess.run([sys.executable, 'C:\\.PythonProjects\\persist\\test_source_dir\\test_source_file.py'] + sys.argv[1:])
    input('Press any key to exit...')
