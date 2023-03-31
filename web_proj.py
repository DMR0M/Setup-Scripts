from pathlib import Path
from typing import Optional
from enum import Enum


class WebTempFileNames(Enum):
    """Web template filenames html, css, javascript"""
    HTML_TEMP_FILE_NAME = 'html_temp.txt'
    CSS_TEMP_FILE_NAME = 'css_temp.txt'
    JS_TEMP_FILE_NAME = 'js_temp.txt'
    
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class WebProjFileNames(Enum):
    HTML_FILE_NAME = 'index.html'
    CSS_FILE_NAME = 'style.css'
    JS_FILE_NAME = 'script.js'
    
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
    

class TemplateMaker:
    _template_file_names = WebTempFileNames.list()
    _web_file_names = WebProjFileNames.list()
    
    def __init__(self, project_name: str, *, 
                 template_path: Optional[Path] = Path('./web_templates')) -> None:
        self.project_path = Path.home() / 'Desktop' / project_name
        self.template_path = template_path
        self.saved_templates = {
            'HTML Template': None,
            'CSS Tempalte': None,
            'JavaScript Template': None,
        }
    
    @classmethod
    @property
    def template_files(cls) -> str:
        return cls._template_file_names
    
    @classmethod
    @property
    def web_files(cls) -> str:
        return cls._web_file_names
        
    def __str__(self) -> str:
        templates = ', '.join(self.template_files)
        return f'{__class__.__name__}:\nProject_Path={self.project_path} Templates=({templates})'
    
    def save_templates(self) -> None:
        # The list of key names of the self.saved_templates instance dictionary
        temp_keys = list(self.saved_templates.keys())
        
        for i, temp in enumerate(self.template_files):
            with open(Path(__file__).parent / self.template_path / temp, 'r', encoding='UTF-8') as f:
                template_str = ''.join(f.readlines())
            self.saved_templates[temp_keys[i]] = template_str
                        
    def setup_project(self) -> None:
        templates = tuple(self.saved_templates.values())
        
        if not all(templates):
            raise ValueError('templates must exist\nuse save_templates() method to save the default templates')
        
        else:        
            try:
                # Create empty project directory
                Path.mkdir(self.project_path)
                for i, file in enumerate(self.web_files):
                    with open(self.project_path / file, 'w', encoding='UTF-8') as f:
                        f.write(templates[i])
            except FileExistsError:
                print('File already exist')


def main():
    # Enter a web project name
    proj_name = input('Enter a web project name: ')
    tm = TemplateMaker(proj_name)
 
    # Default templates
    tm.save_templates()
    tm.setup_project()
    
    

if __name__ == '__main__':
    main()
    
