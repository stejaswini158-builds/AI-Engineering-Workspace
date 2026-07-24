from pydantic import BaseModel, EmailStr


# -------------------------
# Register
# -------------------------

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class RegisterResponse(BaseModel):
    message: str


# -------------------------
# Login
# -------------------------

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str