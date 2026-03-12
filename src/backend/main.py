from routers.regular_file_router import regular_file_router
from fastapi import FastAPI

app = FastAPI()
app.title = "ShowMyData"

app.include_router(regular_file_router)
