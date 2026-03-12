from .consts import FILES_JSON_PATH, BASE_DATA_DIR
from helpers.regular_file import RegularFile
from pathlib import Path
from abc import ABC
import json


class FileManager(ABC):

    @staticmethod
    def scanForFiles(data: dict, base_dir: Path) -> dict:
        """
        Scans for new files and appends them to data dict.

        Args:
            data (dict): json dict

        Returns:
            dict: modified data dict with new files
        """

        current_files_path = {file["path"] for file in data["files"]}

        for file_path in base_dir.iterdir():

            if not file_path.is_file():
                continue

            if file_path.name.startswith("."):
                continue

            relative_path = file_path.relative_to(base_dir).as_posix()

            if relative_path not in current_files_path:
                new_file = RegularFile(relative_path, BASE_DATA_DIR)

                print(new_file.asDict())
                data["files"].append(new_file.asDict())

        return data

    @staticmethod
    def addNewFiles() -> None:
        """
        Iterates over all files in BASE_DATA_DIR and adds new files to FILES_JSON_PATH
        """

        with open(FILES_JSON_PATH, "r") as json_file:
            data = json.load(json_file)

        data = FileManager.scanForFiles(data, BASE_DATA_DIR)

        with open(FILES_JSON_PATH, "w") as json_file:
            json.dump(data, json_file, indent=4)
