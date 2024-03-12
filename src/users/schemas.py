from typing import Any
from uuid import UUID

from pydantic import BaseModel, field_validator


class TunedModel(BaseModel):
    # class Config:
    #     orm_mode = True
    pass


class ShowUser(TunedModel):
    id: UUID
    name: str
    email: str
    is_active: bool


class UserCreate(TunedModel):
    name: str
    email: str
    hashed_password: str

    @field_validator('name')
    @classmethod
    def name_must_contain_space(cls, v):
        if ' ' in v:
            raise ValueError('Имя должно быть без пробелов!')
        return v

    @field_validator('email')
    @classmethod
    def email_must_contain_at(cls, v):
        if '@' not in v:
            raise ValueError('Неправильный электронный адрес!')
        return v




