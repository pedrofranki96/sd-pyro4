import os
import Pyro5.api

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import base64 

command = ''
warehouse_name = ''
private_key = ''
public_key = ''
warehouse = ''

# print('Bem vindo ao sistema de gerenciamento de estoque')
# username = input('Digite seu nome de usuario desejado: ')
username = "pedro"
private_key = RSA.import_key(open('./' + username + '/rsa_key.pem').read())
public_key = RSA.import_key(open('./' + username + '/rsa_key_pub.pem').read())
# print(private_key, 'private_key')
# print(public_key, 'public_key')

# warehouse_name = input('Digite o nome do deposito que deseja acessar: ')
warehouse_name = "pedro.deposito"
# print(warehouse_name, 'warehouse_name')
nameserver = Pyro5.api.locate_ns()
uri = nameserver.lookup('example.deposito')
uri2 = nameserver.lookup("example.callback2")
print(uri2, 'uri2')

# warehouse = Pyro5.api.Proxy(uri)

# message = b'pedro.deposito'
# h = SHA256.new(message)
# signer = PKCS115_SigScheme(keyPair)
# signature = signer.sign(h)
# signature = pkcs1_15.new(private_key).sign(h)

# message = {'product': "agua", 'quantity': 5, 'signature': signature, 'sha256': message }
# print(public_key, 'public_key')
# algo = warehouse.access(username, {'key': public_key})

# add = warehouse.add_product(username, message)

# message2 = {'product': "agua", 'quantity': 2, 'signature': signature }
# remove = warehouse.remove_product(username, message2)
# print(remove)

# if(warehouse_name != 'example.deposito'):
#   print('Deposito nao encontrado')
#   exit()

# while command != 'exit':
#   command = input('Digite o comando desejado: ')

#   match command: 
    
    
#python -m Pyro5.nameserver
