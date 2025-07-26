from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app import models
from sqlalchemy.orm import Session
from ..database import get_db
from app.schemas import TransactionBase, TransactionCreate, TransactionOut

router = APIRouter(prefix="/transactions", tags=["Transactions"])
@router.post("/",response_model=TransactionBase)
async def create_transaction(transaction: TransactionBase, db: Session = Depends(get_db)):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/transactions", response_model = List[TransactionOut])
async def get_all_transactions(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()
    return transactions