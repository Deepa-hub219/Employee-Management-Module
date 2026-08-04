from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
 
import models
import schemas
import crud
 
from database import engine, Base, get_db
 
# Create Tables
Base.metadata.create_all(bind=engine)
 
# FastAPI App
app = FastAPI(title="Employee Management System")
 
# Home API
@app.get("/")
def home():
    return {"message": "Employee Management System API"}
 
 
# Create Employee
@app.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)
 
 
# Get All Employees
@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)
 
 
# Get Employee By ID
@app.get("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
 
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found")
 
    return employee
 
 
# Update Employee
@app.put("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    updated_employee = crud.update_employee(db, employee_id, employee)
 
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found")
 
    return updated_employee
 
 
# Delete Employee
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    deleted_employee = crud.delete_employee(db, employee_id)
 
    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found")
 
    return {"message": "Employee Deleted Successfully"}
 