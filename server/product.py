#nome, descrição, quantidade, preço unitário e estoque mínimo

class Product(object):
    name = ""
    description = "" 
    qtd = 0 
    price = 0.0
    min_qtd = 0

    def __init__(self, name, description, qtd, price, min_qtd):
        self.name = name
        self.description = description 
        self.qtd = qtd
        self.price = price
        self.min_qtd = min_qtd

    