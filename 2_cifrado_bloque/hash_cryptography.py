"""
    EJEMPLO DE USO HASH CON SHA-256
    LIBRERÍA -> cryptography
"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def calculate_hash(route):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend)
    with open(route, 'rb') as file:
        while True:
            block = file.read(65536)
            if not block:
                break
            digest.update(block)
    
    return digest.finalize()

#Main - Ejemplo de uso
route = './ejemplo_real_aes/archivo_original.txt'
hash_file = calculate_hash(route)

print('Has del archivo ' + hash_file.hex())