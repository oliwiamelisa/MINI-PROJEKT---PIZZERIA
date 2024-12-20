from employee import Employee
from phone import Phone

class Waiter(Employee):
    def __init__(self, employee_id: int, name: str, availability: bool, tables: int):
        super().__init__(employee_id, name,role: "Kelner", availability)
        self.tables = tables

    def __str__(self):
        return f"Kelner {self.name} - Obsługiwane stoliki: {self.tables}, Dostępność: {'Tak' if self.availability else 'Nie'}"