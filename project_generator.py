# Script to generate new project structure
import os
import shutil

def create_new_project(project_name):
    """
    Auto-generate project structure
    """
    # Create folders
    os.makedirs(f'{project_name}/data', exist_ok=True)
    os.makedirs(f'{project_name}/output', exist_ok=True)
    os.makedirs(f'{project_name}/logs', exist_ok=True)
    
    # Copy automation_utils.py
    shutil.copy('automation_utils.py', f'{project_name}/')
    
    # Create main.py template
    with open(f'{project_name}/main.py', 'w') as f:
        f.write('''
from automation_utils import *

# Your automation code here

setup_logging()

df = load_csv('data/input.csv')
# Add your steps...
        ''')
    
    print(f"✅ Project {project_name} created!")

# Usage:
# python project_generator.py "06-email-automation"

