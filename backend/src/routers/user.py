from typing import Any, Union

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.crud import create_user as crud_create_user
from src.crud import create_user_item, get_user, get_user_by_email, get_users
from src.database.dependencies import get_db
from src.schemas.item import Item, ItemCreate
from src.schemas.user import User, UserCreate

router = APIRouter()


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Union[Session, Any] = Depends(get_db)) -> Any:
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_create_user(db=db, user=user)


@router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)) -> Any:
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}/items/", response_model=Item)
def create_item_for_user(
    user_id: int, item: ItemCreate, db: Session = Depends(get_db)
) -> Any:
    return create_user_item(db=db, item=item, user_id=user_id)
