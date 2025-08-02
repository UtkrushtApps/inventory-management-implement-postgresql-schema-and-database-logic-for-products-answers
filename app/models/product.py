from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import expression

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, index=True)
    sku = Column(String(64), nullable=False, unique=True, index=True)
    quantity = Column(Integer, nullable=False, default=0)
    last_updated = Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())
