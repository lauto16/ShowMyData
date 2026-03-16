from helpers.consts import EXT_TYPE_MAP
from pathlib import Path
import hashlib
import uuid

class RegularFile:
    """
    Represents a regular file in the user's PC.
    """

    def __init__(self, file_path: str, base_path: str) -> None:
        self.file_path = file_path
        self.base_path = base_path
        self.hash = self.generateHash(file_path, base_path)
        self.type = self.getType(file_path)

    def asDict(self) -> dict:
        return {"path": self.file_path, "hash": self.hash, "type": self.type}

    @staticmethod
    def getType(file_path: str) -> str:

        ext = Path(file_path).suffix.lower().lstrip(".")

        for key, values in EXT_TYPE_MAP.items():
            if ext in values:
                return key

        return "other"

    @staticmethod
    def generateHash(file_path: str, base_path: Path) -> str:
        hasher = hashlib.sha256()

        full_path = base_path / file_path

        with open(full_path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)

        content_hash = hasher.hexdigest()
        unique_part = uuid.uuid4().hex

        return f"{content_hash}_{unique_part}"
