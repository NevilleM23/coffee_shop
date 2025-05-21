class customer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise AttributeError("Coffe name is not changeable")
        if not isinstance(name, str):
            raise TypeError("Name has to be a string")
        if not 3 <= len(name):
            raise  ValueError("Name has to be greater than or equal to three characters")
        self._name = name 
    
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders})

    def create_order(self, cofee, price):
        return Order(self.coffee, price) 
    
    @classmethod
    