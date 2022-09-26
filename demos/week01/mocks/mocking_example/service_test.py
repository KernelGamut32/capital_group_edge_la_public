import unittest
from services.service import Service


class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service()

    def test_service_with_large_quantity(self):
        self.assertEqual(0.25, self.service.get_discount(1001))

    def test_service_with_medium_quantity(self):
        self.assertEqual(0.10, self.service.get_discount(501))

    def test_service_with_small_quantity(self):
        self.assertEqual(0.05, self.service.get_discount(200))

