import os
import Pyro5.api

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

command = ''
warehouse_name = ''
private_key = ''
public_key = ''
warehouse = ''

print('Bem vindo ao sistema de gerenciamento de estoque')
username = input('Digite seu nome de usuario desejado: ')

if(os.path.isdir(username)):
  private_key = RSA.import_key(open('./' + username + '/rsa_key.pem').read())
  public_key = open('./' + username + '/rsa_key_pub.pem').read()
  print(private_key, 'private_key')
  print(public_key, 'public_key')

warehouse_name = input('Digite o nome do deposito que deseja acessar: ')
print(warehouse_name, 'warehouse_name')
nameserver = Pyro5.api.locate_ns()
uri = nameserver.lookup(warehouse_name)
print(uri, 'uri')

warehouse = Pyro5.api.Proxy(uri)

alog = warehouse.access(username, public_key)
print(alog, 'alog')
# if(warehouse_name != 'example.deposito'):
#   print('Deposito nao encontrado')
#   exit()

# while command != 'exit':
#   command = input('Digite o comando desejado: ')

#   match command: 
    
    
#ppython -m Pyro5.nameserver
