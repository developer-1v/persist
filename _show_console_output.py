
import subprocess
import sys

if __name__ == '__main__':
    subprocess.run([sys.executable, 'c:\\.PythonProjects\\persist\\utilities.py'] + sys.argv[1:])
    input('Press any key to exit...')
    sys.exit()
