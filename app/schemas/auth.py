
from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    full_name: str = Field(min_length=2, max_length=150)
    email: str
    phone: str
    password: str = Field(min_length=8)


class VerifyOTPRequest(BaseModel):
    email: str
    otp: str
    channel: str = "email"
