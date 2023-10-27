"""
    EJEMPLO USO AES CON CBC, CFB, OFB
    1) Para usar CBC -> MODE_CBC
    2) Para usar CFB -> MODE_CFB
    3) Para usar OFB -> MODE_OFB
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_aes_key():
    #Cuanto mayor longitud de bits tenga la clave más seguro será el cifrado
    return get_random_bytes(16) 

def generate_vi():
    return get_random_bytes(16)

def encrypt_aes(message, key, vi):
    aes_cipher = AES.new(key, AES.MODE_CBC, vi)
    padded_message = message.ljust((len(message) // 16 + 1) * 16)
    encrypted_message = aes_cipher.encrypt(padded_message.encode())
    return encrypted_message

def decrypt_aes(encrypted_message, key, vi):
    aes_cipher = AES.new(key, AES.MODE_CBC, vi)
    decrypted_message = aes_cipher.decrypt(encrypted_message).decode().rstrip('\0')
    return decrypted_message

#Main - Ejemplo de uso
aes_key = generate_aes_key()
vi = generate_vi()

message = 'Ejemplo de cifrado con AES y VI'

encrypted_message = encrypt_aes(message, aes_key, vi)
print('Mensaje cifrado: ' + str(encrypted_message))

descrypted_message = decrypt_aes(encrypted_message, aes_key, vi)
print('Mensaje descifrado: ' + str(descrypted_message))