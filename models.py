from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


# setting data validation with pydantic

class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Roles(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Roles]
    
class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Roles]]