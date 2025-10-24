from sqlalchemy import Column, Integer, String, Float, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(255), nullable=False)
    customer_email = Column(String(255), nullable=False)
    customer_phone = Column(String(50))
    customer_address = Column(Text)
    payment_method = Column(String(50))
    total_amount = Column(Float, nullable=False)
    status = Column(String(50), default="en cours")
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product_name = Column(String(255))
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    
    order = relationship("Order", back_populates="items")
