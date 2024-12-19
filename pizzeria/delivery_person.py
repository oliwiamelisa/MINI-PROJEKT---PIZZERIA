from employee import Employee

class DeliveryPerson(Employee):
    def __init__(self, employee_id: int, name: str, vehicle: str, availability: bool = True):
        super().__init__(employee_id, name, role="Dostawca", availability=availability)
        self.vehicle = vehicle
        
        def is_on_delivery(self) -> bool:
            """Sprawdza czy dostawca jest obecnie na dostawie."""
            return not self.availability
        
        def __str__(self):
            return f"Dostawca {self.name} (pojazd: {self.vehicle})" 
            
        

