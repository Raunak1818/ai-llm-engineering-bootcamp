from pydantic import BaseModel
from typing import Optional, List, Union

# ******** OPTIONAL NESTED MODEL ***************


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None

# Ex-1
employee = Employee(
    name= "John",
    company= Company(
        name= "OpenAI",
        address= Address(
            street= "123 AI Street",
            city= "San Francisco",
            postal_code= "94105",
        )
    )
)
# print(employee)

# Ex-2
employee = Employee(
    name= "John",
    company= Company(
        name= "OpenAI"
    )
)
# print(employee)


# Ex-3
employee = Employee(
    name= "John"
)
# print(employee)


# ******** MIXED DATA TYPES********


class TextContent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]

article = Article(
    title= "Python",
    sections= [
        TextContent(
            content= "Python is Programming language"
        ),
        ImageContent(
            url= "https://example.com/python.png",
            alt_text= "Python Logo"
        ),
        TextContent(
            content= "Pydantic make data validation simple"
        )
    ]

)
# print(article)





# ******** DEEPLY NESTED STRUCTURE ********

class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class Organization(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address] = []

organisation = Organization(
    name= "Tech Solutions",
    head_quarter= Address(
        street= "123 smth",
        postal_code= "302001",
        city= City(
            name= "Jaipur",
            state= State(
                name= "Rajasthan",
                country= Country(
                    name = "India",
                    code= "IN"
                )
            )
        ) 
    ),
    branches= [
        Address(
          street= "45 Vaishali Nagar",
          postal_code= "302021",
          city= City(
              name= "Jaipur",
              state= State(
                  name= "Rajasthan",
                  country= Country(
                      name= "India",
                      code= "IN"
                  )
              )
          )  
        )
    ]
)

print(organisation)