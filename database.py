from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
 
# MySQL Database URL
DATABASE_URL = "mysql+pymysql://root:Moshika%401294@localhost/employee_db"
 
# Create Engine
engine = create_engine(DATABASE_URL)
 
# Create Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
 
# Base Class
Base = declarative_base()
 
# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 