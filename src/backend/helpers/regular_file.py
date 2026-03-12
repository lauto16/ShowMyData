import hashlib


class RegularFile:
    """
    Represents a regular file in the users pc.
    """
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.hash = RegularFile.generateHash(self.file_path)

    def asDict(self) -> dict:
        """
        Returns the object as a dict. 
        """
        return {
            "path": self.file_path,
            "hash": self.hash
        }
    
    @staticmethod
    def generateHash(str_path: str) -> str:
        """
        Generates the file's unique hash
        Returns:
            (str): Hash
        """
        return hashlib.sha256(str_path.encode()).hexdigest()
