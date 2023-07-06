from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from typing import List, Optional

class DegreeType(Enum):  
    expert = 'expert'
    newbie = 'newbie'
    
    
class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType
    
    
class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=15)
    side: str
    price: float = Field(ge=0)
    amount: float
   