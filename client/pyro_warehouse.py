import os
import Pyro5.api

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import base64 

class PyroWarehouse(object): 
  def __init__(self, name):
    self.name = name
    self.uri = ""
    self.public_key = None
    self.private_key = None
    self.warehouse = None
  
  def connect(self, username, warehouse):
    self.private_key = RSA.import_key(open('./' + username + '/rsa_key.pem').read())
    self.public_key = RSA.import_key(open('./' + username + '/rsa_key_pub.pem').read())

    nameserver = Pyro5.api.locate_ns()
    self.uri = nameserver.lookup('example.deposito')
    self.warehouse = Pyro5.api.Proxy(self.uri)

  def add_product(self, product, quantity):
    message = create_message(product, quantity, message)
    
    return self.warehouse.add_product(self.username, message)

  def remove_product(self, product, quantity):
    message = create_message(product, quantity, message)

    return self.warehouse.remove_product(self.username, message)

  def create_message(self, product, quantity, message):
    message = str(message).encode('utf-8')
    h = SHA256.new(message)
    signature = pkcs1_15.new(self.private_key).sign(h)
    message = {'product': product, 'quantity': quantity, 'signature': signature, 'sha256': message }
    return message
  