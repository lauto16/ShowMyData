from decorators.file_manager import refresh_data_folder
from helpers.consts import FILES_JSON_PATH
from fastapi.responses import JSONResponse
from fastapi import APIRouter
import json

regular_file_router = APIRouter()


@regular_file_router.get("/files")
@refresh_data_folder
def get_files_json() -> JSONResponse:
    """
    Returns the content of the json data file
    """
    data = {}
    with open(FILES_JSON_PATH, "r") as json_file:
        data = json.load(json_file)
    return JSONResponse(data)
 