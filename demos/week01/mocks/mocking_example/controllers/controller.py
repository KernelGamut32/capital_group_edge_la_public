class Controller():
    def __init__(self, service):
        self.service = service

    def get_discounted_price(self, quantity, unit_cost):
        try:
            discount_rate = self.service.get_discount(quantity)
            return quantity * unit_cost * (1 - discount_rate)
        except ValueError:
            return 0
