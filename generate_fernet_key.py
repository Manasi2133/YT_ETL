# Generating Fernet Key
from cryptography.fernet import Fernet

fernet_key = Fernet.generate_key()
print(fernet_key.decode())  # this will print the Fernet Key
