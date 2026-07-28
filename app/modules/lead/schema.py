from pydantic import BaseModel


class LeadCreate(BaseModel):
    gym_id: int
    customer_name: str
    phone: str
    interested_in: str
    source: str
    status: str = "NEW"
    notes: str = ""


class LeadUpdate(BaseModel):
    gym_id: int
    customer_name: str
    phone: str
    interested_in: str
    source: str
    status: str
    notes: str


class LeadResponse(BaseModel):
    id: int
    gym_id: int
    customer_name: str
    phone: str
    interested_in: str
    source: str
    status: str
    notes: str

    model_config = {
        "from_attributes": True
    }