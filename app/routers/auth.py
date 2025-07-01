from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta, UTC
from jose import jwt

router = APIRouter(prefix="/auth", tags=["Auth"])

# Defina sua chave secreta e algoritmo
import os

SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe_default_secret")
ALGORITHM = "HS256"

# Função de autenticação de exemplo
def authenticate_user(username: str, password: str):
    # Substitua pela lógica real de autenticação
    if username == "admin" and password == "senha":
        return {"username": username}
    return None

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    expiration = datetime.now(UTC) + timedelta(hours=1)
    token = jwt.encode({"sub": user["username"], "exp": expiration}, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": token, "token_type": "bearer"}