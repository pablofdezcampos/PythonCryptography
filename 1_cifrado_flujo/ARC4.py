"""
  Ejemplo de Cifrado y Descifrado en Flujo con ARC4
  Para poder usar ARC4 pip install pycryptodome
"""

from Crypto.Cipher import ARC4
import secrets

def arc4_cifrado(texto, clave):
    cifrador = ARC4.new(clave)
    cifrado = cifrador.encrypt(texto)
    return cifrado

def arc4_descifrado(cifrado, clave):
    cifrador = ARC4.new(clave)
    texto_descifrado = cifrador.decrypt(cifrado)
    return texto_descifrado

#Main - Ejemplo de uso
original_text = b"Ejemplo de cifrado en flujo con ARC4"
clave_arc4 = secrets.token_bytes(16)

#Cifrado ARC4
cifrado = arc4_cifrado(original_text, clave_arc4)

print('Texto cifrado: ' + str(cifrado))

#Descifrado ARC4
descifrado = arc4_descifrado(cifrado, clave_arc4)

print('Texto descifrado: ' + str(descifrado))