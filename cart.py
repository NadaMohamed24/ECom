
from sqlalchemy import Column, Integer, Float, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship 
from .base import Base 
from datetime import datetime
from sqlalchemy import CheckConstraint


class Cart(Base):

    __tablename__ = "carts"

    # __table_args__ = (
    #     CheckConstraint("user_id", name="uq_carts_user"),
    # )
 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
 