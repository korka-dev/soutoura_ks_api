from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class OrderItemCreate(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float
    size: Optional[str] = None
    color: Optional[str] = None

class OrderItemResponse(OrderItemCreate):
    id: int

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    customer_name: str
    customer_email: str
    customer_phone: Optional[str] = None
    customer_address: Optional[str] = None
    payment_method: str
    total_amount: float
    items: List[OrderItemCreate]

class OrderUpdate(BaseModel):
    status: Optional[str] = None

class OrderResponse(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    customer_phone: Optional[str]
    customer_address: Optional[str]
    payment_method: str
    total_amount: float
    status: str
    created_at: datetime
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True
