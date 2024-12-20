from employee import Employee
from phone import Phone

class Waiter(Employee):
    def __init__(self, employee_id: int, name: str, availability: bool, table: int):
        super().__init__(employee_id, name,role: "Kelner", availability)
        self.table = table

    def toggle_availability(self):
        self.is_available = not self.is_available

    def take_the_order(self):
        if self.is_available:
            odbierz telefon
            self.toggle_availability()
    
    def __str__(self):
        return f"Kelner {self.name} - Obsługiwane stoliki: {self.tables}, Dostępność: {'Tak' if self.availability else 'Nie'}"