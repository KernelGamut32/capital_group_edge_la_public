from orders.models.order import Order
from orders.repositories.order import OrderRepository


class OrderService():
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def add_new(self, order: Order):
        return self.order_repository.insert(order)

    def get_one(self, order_number):
        return self.order_repository.get_by_number(order_number)
