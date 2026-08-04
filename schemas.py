from pydantic import BaseModel
 
 
class EmployeeBase(BaseModel):
    name: str
    email: str
    phone: str
    designation: str
    salary: float
 
 
class EmployeeCreate(EmployeeBase):
    pass
 
 
class EmployeeResponse(EmployeeBase):
    id: int
 
    class Config:
        from_attributes = True
 