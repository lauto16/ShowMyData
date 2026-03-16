from fastapi import APIRouter, UploadFile, File, HTTPException
from helpers.consts import FILES_JSON_PATH, BASE_DATA_DIR
from decorators.file_manager import refresh_data_folder
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import json


regular_file_router = APIRouter()


@regular_file_router.get("/files")
@refresh_data_folder
def get_files_json() -> JSONResponse:
    """
    Returns the content of the json data file
    """
    with open(FILES_JSON_PATH, "r") as json_file:
        data = json.load(json_file)

    return JSONResponse(data)


@regular_file_router.post("/upload")
@refresh_data_folder
async def upload_file(file: UploadFile = File(...)) -> JSONResponse:
    """
    Uploads a file and saves it in BASE_DATA_DIR
    """

    file_path = Path(BASE_DATA_DIR) / file.filename

    if file_path.exists():
        raise HTTPException(status_code=400, detail="File already exists")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse({"message": "File uploaded successfully"})


@regular_file_router.delete("/files")
@refresh_data_folder
async def delete_files(payload: dict) -> JSONResponse:
    """
    Deletes files from filesystem and JSON
    Expected payload:
    {
        "files": ["path1", "path2"]
    }
    """

    files_to_delete = payload.get("files", [])

    if not files_to_delete:
        raise HTTPException(status_code=400, detail="No files provided")

    with open(FILES_JSON_PATH, "r") as json_file:
        data = json.load(json_file)

    remaining_files = []

    for file in data["files"]:
        if file["path"] in files_to_delete:
            file_path = Path(BASE_DATA_DIR) / file["path"]

            if file_path.exists():
                file_path.unlink()
        else:
            remaining_files.append(file)

    data["files"] = remaining_files

    with open(FILES_JSON_PATH, "w") as json_file:
        json.dump(data, json_file, indent=4)

    return JSONResponse({"message": "Files deleted successfully"})