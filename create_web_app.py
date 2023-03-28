from pathlib import Path
import os
import sys
from enum import Enum
from typing import Optional


class Impls(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class AppTypes(Impls):
    REACT = 'react'
    VUE = 'vue'
    SVELTE = 'svelte'

    # TypeScript Apps
    REACT_TS = 'react-ts'
    VUE_TS = 'vue-ts'
    SVELTE_TS = 'svelte-ts'


class WebApps:
    _enum_app_list = AppTypes.list()

    def __init__(self, app_name: str, 
        *, path_dir: Optional[Path] = Path.home() / 'Desktop'):
        self._app_type = None
        self._app_name = app_name
        self._location = path_dir
        
    def __str__(self, instance, owner):
        return f'Command: npm create vite@latest {self._app_name} -- --template {self._app_type}'

    def create_app(self, app):
        if not app in self._enum_app_list:
            raise ValueError('Must be a valid app type')
        else:
            self._app_type: str = app

            # Go to project directory parent path
            os.chdir(self._location)

            # Create web app in vite
            os.system(f'npm create vite@latest {self._app_name} -- --template {self._app_type}')
            
            # Run npm install in project directory
            os.chdir(self._app_name)
            os.system('npm install')

            # Prompt to run the server
            while True:
                run = input('Do you want to run the server? [y/n]\n')
                match run:
                    case 'y':
                        os.system('npm run dev')
                        sys.exit()
                    case 'n':
                        break
                    case _:
                        print('Invalid input, [y/n] only')
            print(f'Done, creating {self._app_type} project!')


def main():
    project_name = input('Type project name: ')
    app_type = input('Choose [react, vue, svelte]: ')
    
    inst = WebApps(project_name)
    inst.create_app(app_type)


if __name__ == '__main__':
    main()
    
