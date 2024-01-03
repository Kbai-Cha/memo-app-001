from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.crud import get_items
from src.database.dependencies import get_db
from src.schemas.item import Item

router = APIRouter()


@router.get("/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List:
    items = get_items(db, skip=skip, limit=limit)
    return items
