from sqlalchemy.orm import Session
import models
import schemas
 
 
# Create Employee
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
 
 
# Get All Employees
def get_employees(db: Session):
    return db.query(models.Employee).all()
 
 
# Get Employee By ID
def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()
 
 
# Update Employee
def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()
 
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db_employee.phone = employee.phone
        db_employee.designation = employee.designation
        db_employee.salary = employee.salary
 
        db.commit()
        db.refresh(db_employee)
 
    return db_employee
 
 
# Delete Employee
def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()
 
    if db_employee:
        db.delete(db_employee)
        db.commit()
 
    return db_employee
 