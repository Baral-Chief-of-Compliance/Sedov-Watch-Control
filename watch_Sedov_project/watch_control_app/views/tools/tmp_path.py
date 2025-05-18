class TemplatePath(object):
    """Класс для создания пути к шаблонами html"""
    tmp_name : str = ''

    def __init__(self, tmp_name: str):
        self.tmp_name = tmp_name

    def add(self) -> str:
        """Создает путь к файлу add.html в директории"""
        return f'{self.tmp_name}/add.html'
    
    def list(self) -> str:
        """Создает путь к файлу list.html в директории"""
        return f'{self.tmp_name}/list.html'
    
    def update(self) -> str:
        """Создает путь к файлу update.html в директории"""
        return f'{self.tmp_name}/update.html'
    
    def get_path(self, path_to_file: str) -> str:
        """Создает путь к файлу path_to_file.html в директории"""
        return f'{self.tmp_name}/{path_to_file}'