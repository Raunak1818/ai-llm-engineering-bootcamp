from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_name = {"id": 101, "name": "ChaiBar", "is_active": True}

user = User(**input_name)
print(user)