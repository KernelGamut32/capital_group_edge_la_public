class Service():
    def get_discount(self, quantity):
        if quantity <= 0:
            raise ValueError

        if quantity >= 1000:
            return 0.25
        elif quantity < 1000 and quantity >= 250:
            return 0.10
        elif quantity < 250:
            return 0.05
