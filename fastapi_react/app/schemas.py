from pydantic import BaseModel

class TransactionBase(BaseModel):
    amount: float
    category: str
    is_income: bool
    date: str

class TransactionCreate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int

    class Config:
        from_attributes = True
