from pydantic import BaseModel, EmailStr


class GymCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str


class GymUpdate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str


class GymResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    address: str

    model_config = {
        "from_attributes": True
    }