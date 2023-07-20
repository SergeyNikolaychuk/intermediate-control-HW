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
