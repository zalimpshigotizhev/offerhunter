from fastapi import APIRouter
from db.models import User
from db.config import engine, session
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from src.users.schemas import UserCreate, ShowUser


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[ShowUser])
def get_users():
    with session() as connection:
        with connection.begin():
            users = connection.execute(select(User)).all()
            if not users:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Нет пользователей в базе!")

            result = []

            for user in users:
                r = ShowUser(
                    id=user[0].id,
                    name=user[0].name,
                    email=user[0].email,
                    is_active=user[0].is_active
                )
                result.append(r)
            return result


@router.delete("/all_delete/")
def delete_all_users():
    with session() as connection:
        with connection.begin():
            connection.execute(delete(User))



@router.post("/")
def create_user(form_user: UserCreate):
    new_user = User(**form_user.dict())
    with Session(engine) as conn:
        conn.add(new_user)
        conn.commit()
        conn.refresh(new_user)
        return ShowUser(
            id=new_user.id,
            name=new_user.name,
            email=new_user.email,
            is_active=new_user.is_active
        )
