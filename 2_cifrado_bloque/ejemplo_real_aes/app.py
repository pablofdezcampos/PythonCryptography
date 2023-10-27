from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes

from Crypto.Random import get_random_bytes

def generate_aes_key():
    return get_random_bytes(32)

def generate_vi():
    return get_random_bytes(16)

def encrypt_file(file_path, key, vi):
    #rb = lectura binaria
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    
    cipher = Cipher(algorithms.AES(key), modes.CFB(vi), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    #'.enc' -> extensión del archivo nuevo
    #'.wb' -> se abrirá en modo escritura binaria
    with open(file_path + ".enc", 'wb') as file_encrypted:
        file_encrypted.write(ciphertext)
        
def decrypt_file(encrypted_file_path, key, vi):
    #rb = lectura binaria 
    with open(encrypted_file_path, 'rb') as file_encrypted:
        ciphertext = file_encrypted.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(vi), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(padded_data) + unpadder.finalize()

    with open(encrypted_file_path + ".dec", 'wb') as file_decrypted:
        file_decrypted.write(decrypted_data)        
        
#Main - Ejemplo de uso        
aes_key = generate_aes_key()
vi = generate_vi()

file_path = './archivo_original.txt'

#Cifrar el archivo
encrypt_file(file_path, aes_key, vi)

#Descifrar el archivo
#Se aplica +.enc debido a que el fichero cifrado es .txt.enc
decrypt_file(file_path + ".enc", aes_key, vi)