from sqlalchemy import Column, Integer, String, DECIMAL
from database import Base
 
 
class Employee(Base):
    __tablename__ = "employees"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15))
    designation = Column(String(100))
    salary = Column(DECIMAL(10, 2))
 