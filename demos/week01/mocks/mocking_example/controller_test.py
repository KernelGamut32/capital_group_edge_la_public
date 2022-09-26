import unittest
from unittest.mock import Mock
from controllers.controller import Controller
from services.service import Service


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller(Service())

    def test_controller_with_large_quantity(self):
        self.controller.service.get_discount = Mock(return_value=0.25)
        self.assertEqual(
            9752.2425, self.controller.get_discounted_price(1001, 12.99))

    def test_controller_with_medium_quantity(self):
        self.controller.service.get_discount = Mock(return_value=0.10)
        self.assertEqual(
            5857.191, self.controller.get_discounted_price(501, 12.99))

    def test_controller_with_small_quantity(self):
        self.controller.service.get_discount = Mock(return_value=0.05)
        self.assertEqual(
            2468.1, self.controller.get_discounted_price(200, 12.99))

