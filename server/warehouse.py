from __future__ import print_function
import Pyro4
from product import Product
from user import User


class Warehouse(object):
    products = []
    active_users = []
    
    def __init__(self):
        self.contents = [Product("agua", "1 garrafa", 1, 2.50, 5)]

    def access(name, key):
        if any(user.name == name for user in active_users):
            return 'ok'
        else:
            self.active_users.append(User(name, key))

  
def main():
    Pyro4.Daemon.serveSimple(
            {
                Warehouse: "example.warehouse"
            },
            ns = False)

if __name__=="__main__":
    main()