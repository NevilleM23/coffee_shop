class order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self, price):
        if hasattr(self "_name"):
            raise AttributeError("Coffe name cannot be changed")
        if not isinstance(name, float):
            raise TypeError("Name has to be a float")
        if not 1.0 < = price <= 10.0:
            raise ValueError("Price has to be between 1.0 to 10.0")
        self._price = price
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Must be of type Customer")
        self._customer = customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Must be of type Coffee")
        self._coffee = coffee
