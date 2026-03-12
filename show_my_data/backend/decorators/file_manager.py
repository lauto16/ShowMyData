from helpers.file_manager import FileManager
from functools import wraps


def refresh_data_folder(func):
    """
    Refreshes the json data file by adding all new files to it.

    Args:
        func (function): endpoint
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        FileManager.addNewFiles()
        return func(*args, **kwargs)

    return wrapper
