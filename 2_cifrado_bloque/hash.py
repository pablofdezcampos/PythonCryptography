"""
    EJEMPLO DE USO DE HASH - USO SHA-256
    LIBRERÍA -> haslib
"""

import hashlib

def calculate_hash_file(route, algorithm='sha256', block_size=65536):
    """   
        Algoritmo hash a utilizar (por defecto: SHA-256).
        Tamaño del bloque para leer el archivo (por defecto: 64 KB).
    """
    
    hash_obj = hashlib.new(algorithm)
    
    with open(route, 'rb') as file:
        #iter -> crea un iterador
        #lambda: -> envuelve file.read para que pueda ser usado por iter
        #b'' ->  el bucle para cuando devuelva una cada de bytes vacía
        for block in iter(lambda: file.read(block_size), b''):
            hash_obj.update(block)
    
    return hash_obj.hexdigest()


#Main - Ejemplo de uso

#usamos el mismo archivo que para el ejemplo de cifrado de un txt
route_file = './ejemplo_real_aes/archivo_original.txt'
hash_file = calculate_hash_file(route_file)

print('Hash del fichero ' + hash_file)