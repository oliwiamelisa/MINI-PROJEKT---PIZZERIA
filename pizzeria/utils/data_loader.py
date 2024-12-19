import json

class DataLoader:
    @staticmethod
    def load_data(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data