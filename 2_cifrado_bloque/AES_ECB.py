"""
    EJEMPLO USO AES CON ECB
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_aes_key():
    return get_random_bytes(16)

#AES ECB
def encrypt_aes_ecb(mensaje, clave):
    aes_cipher  = AES.new(clave, AES.MODE_ECB)
    padded_message = mensaje.ljust((len(mensaje) // 16 + 1) * 16)
    encrypted_message = aes_cipher.encrypt(padded_message.encode())
    return encrypted_message

def decrypt_aes_ecb(mensaje_ecriptado, clave) :
    aes_cipher = AES.new(clave, AES.MODE_ECB)
    decrypt_message = aes_cipher.decrypt(mensaje_ecriptado).decode().rstrip('\0')
    return decrypt_message

#Main - Ejemplo de uso
aes_ebc_key = generate_aes_key()

mensaje = "Ejemplo de cifrado con AES y ECB"

encrypted_mensaje = encrypt_aes_ecb(mensaje, aes_ebc_key)
print('Mensaje cifrado: ' + str(encrypted_mensaje))

descrypted_mensaje = decrypt_aes_ecb(encrypted_mensaje, aes_ebc_key)
print('Mensaje descifrado: ' + str(descrypted_mensaje))