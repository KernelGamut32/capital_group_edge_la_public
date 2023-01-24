from pydantic import BaseModel
from orders.models.product import Product


class Order(BaseModel):
    id: int
    order_number: str
    product: Product
    quantity: int
    total: float
