from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class TodoCreate(BaseModel):
    description: str
    scheduled_at: datetime
    status: str = "Todo"


class TodoUpdate(BaseModel):
    description: Optional[str] = None
    scheduled_at: Optional[datetime] = None
    status: Optional[str] = None


class TodoResponse(BaseModel):
    id: str
    description: str
    scheduled_at: datetime
    status: str
    created_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)