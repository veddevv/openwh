import os
import subprocess
from pathlib import Path
import platform

# Define file path using pathlib
if platform.system() == 'Windows':
    file_path = Path("C:\\Users\\User\\Documents\\data.txt")
else:
    file_path = Path("/home/user/documents/data.txt")  # Linux

# Read the file
try:
    with open(file_path, 'r') as file:
        data = file.read()
except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")
    exit(1)

# Execute a command
if platform.system() == 'Windows':
    subprocess.run(["dir"], shell=True)  # Windows command
else:
    subprocess.run(["ls", "-l"])  # Linux command to list directory
