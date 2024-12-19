class Customer:
    def __init__(self, name: str, surname: str, phone_number: str, adress: str):
        self.name = name
        self.surname = surname
        self.phone_number = phone
        self.adress = adress
    
    def __str__(self):
        return f"{self.name} {self.surname}, {self.phone_number}, {self.adress}"
    