from routers.regular_file_router import regular_file_router
from fastapi.middleware.cors import CORSMiddleware
from routers.auth_router import auth_router
from fastapi import FastAPI

app = FastAPI()
app.title = "ShowMyData"

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(regular_file_router)
app.include_router(auth_router)
