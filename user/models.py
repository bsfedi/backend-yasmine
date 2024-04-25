from typing import Optional
from pydantic import BaseModel
from datetime import date , datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    # id:str
    nom: Optional[str]
    prenom: Optional[str]
    telephone: Optional[str]
    date_naissance : datetime
    adresse_mail : Optional[str]
    role: Optional[str] = ""
    adresse: Optional[str]
    password :Optional[str]
    

class User_login(BaseModel):
    adresse_mail: EmailStr
    password: str