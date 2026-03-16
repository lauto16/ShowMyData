from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DATA_DIR = BASE_DIR / "data"
FILES_JSON_PATH = BASE_DIR / "db" / "files.json"
EXT_TYPE_MAP = {
    "text": {"txt", "md", "rtf", "log"},
    "code": {
        "py",
        "js",
        "ts",
        "java",
        "c",
        "cpp",
        "h",
        "hpp",
        "cs",
        "go",
        "rs",
        "php",
        "rb",
        "swift",
        "kt",
        "kts",
        "scala",
        "sh",
        "bash",
        "zsh",
        "ps1",
    },
    "web": {"html", "htm", "css", "scss", "sass", "json", "xml", "yaml", "yml"},
    "image": {"jpg", "jpeg", "png", "gif", "bmp", "webp", "svg", "ico", "tiff", "tif"},
    "video": {"mp4", "mkv", "mov", "avi", "wmv", "flv", "webm", "m4v"},
    "audio": {"mp3", "wav", "flac", "aac", "ogg", "m4a", "wma"},
    "document": {"pdf", "doc", "docx", "odt", "xls", "xlsx", "ppt", "pptx"},
    "archive": {"zip", "rar", "7z", "tar", "gz", "bz2", "xz"},
    "executable": {"exe", "msi", "bin", "app", "apk", "deb", "rpm"},
    "database": {"db", "sqlite", "sqlite3", "sql", "mdb"},
    "config": {"ini", "cfg", "conf", "env", "toml"},
}


if __name__ == "__main__":
    print(FILES_JSON_PATH)