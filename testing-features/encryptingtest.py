from cryptography.Fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt("test")
print(f.decrypt(token))