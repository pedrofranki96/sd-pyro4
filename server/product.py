#nome, descrição, quantidade, preço unitário e estoque mínimo

class Product(object):
    name = ""
    description = "" 
    quantity = 0 
    price = 0.0
    min_qtd = 0

    def __init__(self, name, description, quantity, price, min_qtd):
        self.name = name
        self.description = description 
        self.quantity = quantity
        self.price = price
        self.min_qtd = min_qtd

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description
    
    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price
    
    def getMinQtd(self):
        return self.min_qtd
    
    def setName(self, name):
        self.name = name
    
    def setDescription(self, description):
        self.description = description
    
    def setQuantity(self, quantity):
        self.quantity = quantity

    def setPrice(self, price):
        self.price = price
    
    def setMinQtd(self, min_qtd):
        self.min_qtd = min_qtd

    

    