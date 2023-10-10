import sys
import Pyro4
from person import Person

if sys.version_info<(3,0):
    input = raw_input

uri = input("Enter the uri of the warehouse: ").strip()
warehouse = Pyro4.Proxy(uri)
janet = Person("Janet")
henry = Person("Henry")
janet.visit(warehouse)
henry.visit(warehouse)

# message = b'To be signed'
# key = RSA.import_key(open('./rsa_key.pem').read())
# print(key)
# h = SHA256.new(message)
# print(h)
# signature = pkcs1_15.new(key).sign(h)

# print(signature)

# f = SHA256.new(message)

# public_key = RSA.import_key(open('./rsa_key_pub.pem').read())
# p = open('./rsa_key_pub.pem').read()
# print(p, 'public keydhdhdh')
# print(public_key, 'public key')
# try:
#     pkcs1_15.new(public_key).verify(f, signature)
#     print("The signature is valid.")
# except (ValueError, TypeError):   
#     print("The signature is not valid.")