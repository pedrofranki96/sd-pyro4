import os
import Pyro5.api
from server.warehouse import Warehouse

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import base64 

command = ''
warehouse_name = ''
private_key = ''
public_key = ''
warehouse = Warehouse()

username = "pedro"

warehouse_name = "pedro.deposito"
print(warehouse_name, 'warehouse_name')
nameserver = Pyro5.api.locate_ns()
uri = nameserver.lookup(warehouse_name)

private_key = RSA.import_key(open('./' + username + '/rsa_key.pem').read())
public_key = RSA.import_key(open('./' + username + '/rsa_key.pem').read())
print(public_key, type(public_key), 'public_key')

message = b'pedro.deposito'
h = SHA256.new(message)
signature = pkcs1_15.new(private_key).sign(h)

print(signature, type(signature), 'ddddd')
message1 = {'product': "agua", 'quantity': 6, 'signature': signature, 'sha256': message }
algo = warehouse.access(username, {'key': public_key})

add = warehouse.add_product(username, message1)

prited_warehouse = warehouse.print_warehouse()
print(prited_warehouse, 'prited_warehouse')

message2 = {'product': "agua", 'quantity': 2, 'signature': signature, 'sha256': message }

removed = warehouse.remove_product(username, message2)
print(removed, 'removed')

prited_warehouse = warehouse.print_warehouse()
print(prited_warehouse, 'prited_warehouse')
