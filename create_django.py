from pathlib import Path
import os
import shutil
import sys
from tqdm import tqdm
from typing import Optional, Iterable


def create_project(dir_name: str, package_name: str, *,
        parent_dir: Optional[str] =  Path.home() / 'Desktop',
        make_files: Optional[Iterable] = ['main.py', '__init__.py'],
        dependencies: Optional[Path] = 'dependencies/requirements.txt') -> None:
    """Create a python project with venv"""
    curr_path: Path = Path.cwd()

    try:
        # Go to Desktop Directory
        os.chdir(parent_dir) 
    
        # Create project folder
        Path.mkdir(dir_name)
        os.chdir(project := Path(parent_dir / dir_name))
        os.system(f'python -m venv {project}')

        # Create files in project folder
        Path.mkdir(package_name)
        os.chdir(package_name)

        # Copy the list of dependencies to created project folder
        shutil.copy(curr_path / 'Django_req' / 'requirements.txt', Path.cwd().parent)

        for make in tqdm(make_files, desc='Creating files in package'):
            Path.touch(make)
        
    except FileExistsError:
        print('File exists')


def main() -> None:
    project_name = input('Type a project name: ')
    package_name = input('Type a package name: ')
    
    create_project(project_name, package_name)

    print('Successful')


if __name__ == '__main__':
    main()


