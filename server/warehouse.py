from __future__ import print_function
import Pyro5.api
from product import Product
from user import User

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

@Pyro5.api.expose
class Warehouse(object):
    products = []
    active_users = []
    
    def __init__(self):
        p = Product("agua", "1 garrafa", 1, 2.50, 5)
        print(str(p), 'product')
        self.products = [p]
        print(self.products, 'contents')

    def imprime_algo(self):
        print("algo")
        print(str(self.products), 'products')
        return "algo"

    def access(self, name, key):
        if any(user.name == name for user in self.active_users):
            return 'ok'
        else:
            self.active_users.append(User(name, key))
            return 'ok'

    def new_product(self, user, name, description, quantity, price, min_qtd):
        self.contents.append(Product(name, description, quantity, price, min_qtd))

    def entry_product(self, user, name, quantity):
        for product in self.contents:
            if product.name == name:
                product.quantity += quantity
                return 'ok'
        return 'product_not_found'
    
    def remove_product(self, user, name, quantity):
        for product in self.contents:
            if product.name == name:
                if product.quantity < quantity:
                    return 'not_enough_quantity'
                product.quantity -= quantity
                return 'ok'
        return 'product_not_found'

    def verify_user_messsage(self, user, message, signature):
        for user in self.active_users:
            if user.name == name:
                public_key = RSA.import_key(user.key)
                hash = SHA256.new(message)
                try:
                    pkcs1_15.new(public_key).verify(hash, signature)
                    return 'ok'
                except (ValueError, TypeError):
                    return 'invalid message'

  
def main():
    daemon = Pyro5.api.Daemon()             # make a Pyro daemon
    uri = daemon.register(Warehouse)
    ns = Pyro5.api.locate_ns()
    ns.register("pedro.deposito", uri)   # register the object with a name in the name server
    print("Ready.")
    daemon.requestLoop()              

if __name__=="__main__":
    main()