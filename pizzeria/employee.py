

class Employee:
    def __init__(self, employee_id: int, name: str, role: str, availability: bool = True):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.availability = availability
        
    def is_available(self):
        """Sprawdza czy pracownik jest dostępny"""
        if self.availability == True :
            return f"{self.name} {self.role} - Dostępny"
        elif self.availability == False:
            return f"{self.name} {self.role} - Zajęty"
        