from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class test_schema(BaseModel):
    name: str
    email: EmailStr
    

