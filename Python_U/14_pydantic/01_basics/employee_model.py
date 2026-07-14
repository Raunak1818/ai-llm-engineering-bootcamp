from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    name: str = Field(
        ...,
        min_length= 3,
        max_length= 30,
        description= "Employee Name",
        examples= "Raunak Jaiswal",
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge= 10000,
    )

class User(BaseModel):
    email: str = Field(
        ...,
        pattern = r''
    )
    phone: str = Field(
        ...,
        pattern = r''
    )
    age: int = Field(
        ...,
        ge= 0,
        le= 150,
        description= "Age in years"
    )
    discount: float = Field(
        ...,
        ge= 0,
        le= 100,
        description= "Discount Percentage"
    )



employee = Employee(
    name="Raunak Jaiswal",
    salary=50000
)

print(employee)



user = User(
    email="raunak@gmail.com",
    phone="9876543210",
    age=22,
    discount=15
)

print(user)