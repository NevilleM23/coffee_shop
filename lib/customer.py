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
    def most_aficionado (cls, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeErrer("Must be of type Coffee")

        coffee_orders = [o for o in Order.all if o.coffee == coffee]

        if not coffee_orders:
            return None

        return max(
            set(o.customer for o in coffee_orders),
            key = lambda c:sum(o.price for o in coffee_rders if o.custmer == c)
        )
