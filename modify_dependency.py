from pathlib import Path
from typing import Optional
import os
import json


class Dependency:
    def __init__(self,
            *, path_dir: Optional[Path] = Path('./Django_req/requirements.txt')) -> None:
        self._data = None
        self._dependencies = None
        self._path_file = path_dir
    
    def __str__(self) -> str:
        return f'Dependency_file={os.path.basename(self._path_file)}\n' \
               f'Relative_path={self._path_file}'

    @property
    def dependencies(self) -> json:
        with open(self._path_file, 'r') as f:
            list_dep = [
                        tuple(item.strip().split('=='))
                        for item in f.readlines()
                    ]
        return json.dumps(dict(list_dep), indent=4)
            
    # Modify the dependency txt file based on given dict argument
    def change_req(self, data: dict) -> None:
        self._data = data
        self._dependencies = [
                    '=='.join(item)
                    for item in list(self._data.items())
                ]
        with open(self._path_file, 'w') as f:
            for dep in self._dependencies:
                f.write(f'{dep}\n')

    # Create new dependency txt file
    def create_req(self, file_path: Path, data: dict) -> None:
        self._data = data
        self._dependencies = [
                    '=='.join(item)
                    for item in list(self._data.items())
                ]

        if not file_path.endswith('.txt'):
            raise ValueError('File must be a txt file')
        else:
            Path.touch(file_path)
            with open(file_path, 'w') as f:
                f.writelines(self._dependencies)


def main():
    dependencies = {
                'Django': '4.1.4',
                'pandas': '1.5.1',
            }
    m = Dependency()

    # Uncomment this line for changing
    # m.change_req(dependencies)
    
    print(m)
    print(m.dependencies)


if __name__ == '__main__':
    main()

