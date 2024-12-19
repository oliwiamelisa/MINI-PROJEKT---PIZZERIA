from customer import Customer
from pizza import Pizza
from enums.delivery_method import DeliveryMethod
from delivery_person import DeliveryPerson



class Order:
    def __init__(self, order_id: int, customer: Customer, pizza: Pizza, delivery_method: DeliveryMethod, delivery_person: DeliveryPerson, table_number=None):
        self.order_id = order_id
        self.customer = customer
        self.pizza = pizza
        self.delivery_method = delivery_method
        self.table_number = table_number
        self.delivery_person = None
        
    def __str__(self):
        if self.delivery_method == DeliveryMethod.DELIVERY:
            return f"Dostawa: {self.pizza} dla {self.customer.name} na adres {self.customer.adress} - (Numer zamówienia: {self.order_id})"
        elif self.delivery_method == DeliveryMethod.ON_SITE:
            return f"Na miejscu: {self.pizza} dla {self.customer.name} do stolika nr {self.table_number} - (Numer zamówienia: {self.order_id})"
        
        
