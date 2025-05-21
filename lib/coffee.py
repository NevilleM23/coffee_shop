class coffee:

    all = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if not isinstance(name, str):
            raise TypeErrer("Name should be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 to 15 characters")
        self._name = name
    
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def  customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.rders()
        if not orders:
            return 0
        return sum(order.price for orders in orders) / len(orders)
