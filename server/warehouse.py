import Pyro5.api
from product import Product
from user import User

from Crypto.Signature import pkcs1_15
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import base64 

@Pyro5.api.expose
class Warehouse(object):
    products = []
    active_users = []
    
    def __init__(self):
        p = Product("agua", "1 garrafa", 1, 2.50, 5)
        p2 = Product("refri", "Garrafa", 1, 3.50, 5)
        self.products = [p, p2]

    def print_warehouse(self):
        cast_products = []
        for product in self.products:
            cast_products.append(product.__dict__)
        return cast_products

    def access(self, name, key):
        if any(user.name == name for user in self.active_users):
            return 'ok'
        else:
            self.active_users.append(User(name, key))
            return 'ok'

    def add_product(self, user, message):
        if self.verify_user_messsage(user, message['sha256'], message['signature']) == 'ok':
            for product in self.products:
                if product.name == message['product']:
                    print(product.quantity, message['quantity'], 'product.quantity')
                    product.setQuantity(product.quantity + message['quantity'])
                    return 'produto adicionado'
            return 'product_not_found'
   
    
    def remove_product(self, user, message):
        if self.verify_user_messsage(user, message['sha256'], message['signature']) == 'ok':
            for product in self.products:
                if product.name == message['product']:
                    if product.quantity < message['quantity']:
                        return 'not_enough_quantity'

                    product.setQuantity(product.quantity - message['quantity'])
                    return 'produto removido'
            return 'product_not_found'

    def verify_user_messsage(self, user, message, signature):
        for active_user in self.active_users:
            if active_user.name == user:
                public_key = active_user.key['key']
                print(public_key, type(public_key), 'public_key')

                print(signature, type(signature), 'warehouse signature')
                h = SHA256.new(b'pedro.deposito')
                pkcs1_15.new(public_key).verify(h, signature)
                print("The signature is valid.")
                return 'ok'
              
class CallbackServer(object):
    @Pyro5.api.expose
    @Pyro5.api.oneway
    def doCallback(self, callback):
        print("\n\nserver: doing callback 1 to client")
        callback._pyroClaimOwnership()
        try:
            callback.call1()
        except Exception:
            print("got an exception from the callback:")
            print("".join(Pyro5.errors.get_pyro_traceback()))
        print("\n\nserver: doing callback 2 to client")
        try:
            callback.call2()
        except Exception:
            print("got an exception from the callback:")
            print("".join(Pyro5.errors.get_pyro_traceback()))
        print("server: callbacks done.\n")
  
def main():
    daemon = Pyro5.api.Daemon()             # make a Pyro daemon
    uri = daemon.register(Warehouse)
    uri2 = daemon.register(CallbackServer)
    ns = Pyro5.api.locate_ns()
    ns.register("example.deposito", uri)   # register the object with a name in the name server
    ns.register("example.callback2", uri2)
    print("Ready.")
    daemon.requestLoop()              

if __name__=="__main__":
    main()