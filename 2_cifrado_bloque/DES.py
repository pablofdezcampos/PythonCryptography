"""
    Librería pycryptome - EJEMPLO USO DES CON ECB
"""

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def generate_des_key():
    return get_random_bytes(8)

def encrypt_des(mensaje, clave):
    des_cipher = DES.new(clave,  DES.MODE_ECB)
    
    #Esta línea asegura que sea un múltiplo de 8 bytes | ljust -> agrega caracteres hacia la derecha hasta que tenga la longitud deseada
    # // -> división entera en python | 8+1 -> añade 1 al número de bloques para que siempre haya espacio para al menos un bloque adicional
    padded_message = mensaje.ljust((len(mensaje) // 8 + 1) * 8)
    
    encrypted_message = des_cipher.encrypt(padded_message.encode())
    return encrypted_message

def descrypt_des(mensaje_encriptado, clave):
    des_cipher = DES.new(clave, DES.MODE_ECB)
    
    #Esta línea el final elimina cualquier carácter nulo al final no deseado
    decrypted_message = des_cipher.decrypt(mensaje_encriptado).decode().rstrip('\0')
    
    return decrypted_message

#Main - Ejemplo de uso
des_key = generate_des_key()

mensaje = "Ejemplo de cifrado con DES y ECB"

encrypted_mensaje = encrypt_des(mensaje, des_key)
print('Mensaje cifrado: ' + str(encrypted_mensaje))

decrypted_mensaje = descrypt_des(encrypted_mensaje, des_key)
print('Mensaje descifrado: ' + str(decrypted_mensaje))