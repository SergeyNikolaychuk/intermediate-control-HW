class Notebook:
    def init(self, brand, model, ram, storage, os, color):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage
        self.os = os
        self.color = color

    def str(self):
        return f"Notebook(brand='{self.brand}', model='{self.model}', ram={self.ram}, storage={self.storage}, os='{self.os}', color='{self.color}')"

class NotebookShop:
    def init(self, notebooks):
        self.notebooks = notebooks

    def filter_notebooks(self):
        min_ram = int(input("Enter the minimum RAM size (in GB): "))
        color = input("Enter the color: ")
        min_storage = int(input("Enter the minimum storage size (in GB): "))

        return [notebook for notebook in self.notebooks if notebook.ram >= min_ram and notebook.color.lower() == color.lower() and notebook.storage >= min_storage]
