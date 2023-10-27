""" 
    Ejemplo de Cifrado y Descifrado en Flujo con XOR
    Se aplica bit a bit
"""

import secrets

#Generamos la clave de forma aleatoria
len_clave = 16
clave_xor = secrets.token_bytes(len_clave)

def xor_cifrado(texto, clave):
    
    cifrado = []
    
    for i in range(len(texto)):
        cifrado.append(texto[i] ^ clave[i % len(clave)])
        
    return bytes(cifrado)        

def xor_descrifrado(texto, clave):
    return xor_cifrado(texto, clave)

#Main - Ejemplo de uso
original_text = b"Ejemplo de cifrado en Flujo con Python"

#Cifrado XOR
cifrado = xor_cifrado(original_text, clave_xor)

print('Texto cifrado: ' + str(cifrado))

#Descifrado XOR con clave aleatoria
texto_descifrado = xor_descrifrado(cifrado, clave_xor)

print('Texto descifrado: ' + str(texto_descifrado))