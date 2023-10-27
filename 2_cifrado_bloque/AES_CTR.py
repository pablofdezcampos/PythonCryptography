"""
    EJEMPLO USO AES CON CTR
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

clave_aes = get_random_bytes(16)

contador = Counter.new(64, prefix=b'\x00' * 8, initial_value=0)

mensaje = "Ejemplo de cifrado con AES y CTR"
bytes_mensaje = mensaje.encode('utf-8')

cipher = AES.new(clave_aes, AES.MODE_CTR, counter=contador)
encrypte_mensaje = cipher.encrypt(bytes_mensaje)
print('Mensaje cifrado: ' + str(encrypte_mensaje))

"""
    Hay que reiniciar el objeto porque no deja poder desencriptar una vez has encriptado
    TypeError: decrypt() cannot be called after encrypt()
"""
cipher_descifrado = AES.new(clave_aes, AES.MODE_CTR, counter=contador)
descrypted_mensaje = cipher_descifrado.decrypt(encrypte_mensaje)
print('Mensaje descifrado: ' + descrypted_mensaje.decode())