import unittest
from orders.models.product import Product
from orders.models.order import Order
from orders.repositories.product import ProductRepository
from orders.repositories.order import OrderRepository


class TestOrderRepository(unittest.TestCase):
    def setUp(self):
        self.productRepository = ProductRepository()
        self.orderRepository = OrderRepository(self.productRepository)
        self.inserted_product = self.productRepository.insert(Product(id=0, product_number="XXX111",
                                                                      description="Sample Description", unit_cost=1.99))
        self.inserted_order = \
            self.orderRepository.insert(Order(
                id=0, order_number="12345678", product=self.inserted_product, quantity=1, total=1.99))

    def tearDown(self):
        self.orderRepository.delete(self.inserted_order.id)
        self.productRepository.delete(self.inserted_product.id)

    def test_get_by_number(self):
        get_order = self.orderRepository.get_by_number(
            self.inserted_order.order_number)
        self.assertEqual(get_order, self.inserted_order)
