from watch_control_app.urls import app_name


def get_success_url(base_url_name: str) -> str:
    """Получить полный путь url для success_url"""
    return f'{app_name}:{base_url_name}_list'