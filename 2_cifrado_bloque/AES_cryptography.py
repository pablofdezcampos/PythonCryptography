"""
    Ejemplo de algoritmo de cifrado AES con librería cryptography
    Para usar crytography -> pip install cryptography
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes

from Crypto.Random import get_random_bytes

#Genera una clave AES de 256 bits o 32 bytes
def generate_aes_key():
    return get_random_bytes(32)

#Genera un vector de inicialización de 128 bits
def generate_vi():
    return get_random_bytes(16)

def encrypt_aes(mensaje, clave, vi):
    
    #Esta línea crea objetos de relleno usando el esquema de relleno PKCS7
    #PKCS7 -> crea objeto de relleno PKCS7 con un tamaño de bloque igual al bloque del algoritmo AES
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    
    padded_data = padder.update(mensaje.encode()) + padder.finalize()
    
    cipher = Cipher(algorithms.AES(clave), modes.CFB(vi), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    return ciphertext

def descrypt_aes(ciphertext, clave, vi):
    cipher = Cipher(algorithms.AES(clave), modes.CFB(vi), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    #Elimina el relleno después del cifrado para recuperar el mensaje original
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_mensaje = unpadder.update(padded_data) + unpadder.finalize()
    
    return decrypted_mensaje

#Main - Ejemplo de uso
aes_key = generate_aes_key()
vi = generate_vi()

mensaje = "Ejemplo de uso de cifrado AES con Cryptography"

encrypted_mensaje = encrypt_aes(mensaje, aes_key, vi)
print('Mensaje encriptado: ' + str(encrypted_mensaje))
    
descrypted_mensaje = descrypt_aes(encrypted_mensaje, aes_key, vi)
print('Mensaje descifrado: ' + str(descrypted_mensaje))   