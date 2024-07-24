# many_to_many.py

class Coffee:
    def __init__(self, name):
        self._name = name
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        raise AttributeError("Name cannot be changed")
    
    def add_order(self, order):
        if isinstance(order, Order):
            self._orders.append(order)
        else:
            raise ValueError("Order must be an instance of Order")
    
    def orders(self):
        return self._orders
    
    def customers(self):
        return list(set(order.customer for order in self._orders))
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        total_price = sum(order.price for order in self._orders)
        return total_price / self.num_orders() if self.num_orders() > 0 else 0

class Customer:
    def __init__(self, name):
        self._name = name
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (1 <= len(new_name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = new_name
    
    def add_order(self, order):
        if isinstance(order, Order):
            self._orders.append(order)
        else:
            raise ValueError("Order must be an instance of Order")
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(order.coffee for order in self._orders))


class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = price
        self.customer = customer
        self.coffee = coffee
        coffee.add_order(self)
        customer.add_order(self)
    
    @property
    def price(self):
        return self._price
