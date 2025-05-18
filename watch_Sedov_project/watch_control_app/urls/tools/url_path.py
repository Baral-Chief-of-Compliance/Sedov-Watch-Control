class UrlPath(object):
    """Класс для создания наименования для url"""
    base_name : str = ""

    def __init__(self, base_name: str):
        self.base_name = base_name

    def add(self) -> str:
        """Возращает наименование base_name_add"""
        return f'{self.base_name}_add'
    
    def update(self) -> str:
        """Возращает наименование base_name_update"""
        return f'{self.base_name}_update'
    
    def list(self) -> str:
        """Возращает наименование base_name_list"""
        return f'{self.base_name}_list'
    
    def delete(self) -> str:
        """Возращает наименование  base_name_delete"""
        return f'{self.base_name}_delete'
    
    def url_name(self, url_name: str) -> str:
        """Возращает наименование base_name_url_name"""
        return f'{self.base_name}_{url_name}'