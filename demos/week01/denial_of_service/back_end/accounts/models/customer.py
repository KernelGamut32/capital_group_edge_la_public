from pydantic import BaseModel
from accounts.models.address import Address


class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Address
    email_address: str
