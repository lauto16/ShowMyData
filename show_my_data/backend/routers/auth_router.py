from fastapi import APIRouter, HTTPException
from helpers.consts import PASSWORDS_PATH
from pydantic import BaseModel
import json

auth_router = APIRouter()


class LoginRequest(BaseModel):
    password: str


@auth_router.post("/login")
def login(data: LoginRequest):
    try:
        with open(PASSWORDS_PATH, "r") as f:
            content = json.load(f)

        valid_passwords = content.get("passwords", [])
        
        if data.password in valid_passwords:
            return {"success": True}

        raise HTTPException(status_code=401, detail="Invalid password")

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Passwords file not found")
