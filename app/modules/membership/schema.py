from pydantic import BaseModel


class MembershipCreate(BaseModel):
    gym_id: int
    name: str
    duration_months: int
    price: float
    joining_fee: float = 0
    description: str
    is_active: bool = True


class MembershipUpdate(BaseModel):
    gym_id: int
    name: str
    duration_months: int
    price: float
    joining_fee: float = 0
    description: str
    is_active: bool = True


class MembershipResponse(BaseModel):
    id: int
    gym_id: int
    name: str
    duration_months: int
    price: float
    joining_fee: float
    description: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }