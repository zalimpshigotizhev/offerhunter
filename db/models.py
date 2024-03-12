from sqlalchemy import UUID
import uuid
from sqlalchemy.orm import declarative_base
import sqlalchemy


Base = declarative_base()



class User(Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    is_active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    def __repr__(self):
        return f"<User(email={self.email})>"