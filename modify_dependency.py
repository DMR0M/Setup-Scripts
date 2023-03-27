from pathlib import Path
from typing import Optional
import json


class Modify:
    def __init__(self, data: dict,
            *, path_dir=Path('./Django_req/requirements.txt')):
        self._data = data
        self._path_file = path_dir
    
    def __get__(self, instance, owner):
        return f'Data:\n {json.dumps(self._data, indent=4)}'

    def modify_req(self):
        with open(self._path_file, 'w') as f:
            pass

    def create_req(self, file_path: Path):
        Path.touch(file_path)
        with open(file_path, 'w') as f:
            pass


def main():
    pass


if __name__ == '__main__':
    main()

