from fastapi import APIRouter

regular_file_router = APIRouter()

@regular_file_router.get('/file')
def get_regular_file(file_hash: FileHash) -> FileResponse:
    pass