"""
    EJEMPLO DE USO ELGAMAL
"""

from Crypto.PublicKey import ElGamal
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

random_generator = Random.new().read
key = ElGamal.generate(2048, random_generator)

public_key = key.publickey()
private_key = key

mensaje = b'Ejemplo de uso de ElGamal'

cipher = PKCS1_OAEP.new(public_key)
cifrado = cipher.encrypt(mensaje)

print('Mensaje cifrado: ' + str(cifrado))

cipher = PKCS1_OAEP.new(private_key)
descifrado = cipher.decrypt(cifrado)

print('Mensaje descifrado: ' + str(descifrado))