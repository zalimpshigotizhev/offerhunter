from sqlalchemy.orm import Session

from db.models import User
from src.schema import UserCreate


class UserDAL:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: UserCreate):
        new_user = User(**user.dict())
        self.session.add(new_user)
        self.session.flush()
        return new_user