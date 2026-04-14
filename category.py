"""
3. Category Entity:
Description: Represents a category of products.
Attributes:- id (Int): Primary key.
- name (String): Name of the category.
- products (Relation): List of products that belong to this category
"""





from sqlalchemy import Column, Integer,Float, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship 
from .base import Base 
from datetime import datetime
from sqlalchemy import CheckConstraint


class Category(Base):
    __tablename__ = "categories"
 
    id   = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
 
    # relations ***********
    products = relationship("Product", back_populates="category")