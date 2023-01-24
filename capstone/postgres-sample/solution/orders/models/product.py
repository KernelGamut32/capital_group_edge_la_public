from pydantic import BaseModel


class Product(BaseModel):
    id: int
    product_number: str
    description: str
    unit_cost: float
