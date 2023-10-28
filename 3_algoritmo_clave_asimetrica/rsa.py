"""
    EJEMPLO DE USO RSA
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

""" 
    65537 -> exponente público en un par de claves RSA
          -> 10000000000000001 solo dos bits en su representación binaria
          -> es lo suficiente grande para proporcionar seguridad adecuada.
    
    2048 -> tamaño de la clave RSA en bits, está recomendado 3072 bits o 4096 bits
    
    Ambos valores son comunes y proporcionan un buen equilibrio entre seguridad y rendimiento.
"""
        
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

"""
    PEM -> es el formato de codificación, convierte los datos binarios en texto ASCII
    PKCS8 -> es un estándar de sintaxis para la información de clave privada
    NoEncryption -> especifica que la clave privada no será no se cifrará durante la serialización.
                 -> en un entorno de produción sería vital cifrar la clave privada con una contraseña para protegerla.
"""
private_pem = private_key.private_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PrivateFormat.PKCS8,
    encryption_algorithm = serialization.NoEncryption()   
)

"""
    SubjectPublicKeyInfo -> es un estándar que define la sintaxis para la información de la clave pública
"""
public_pem = public_key.public_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PublicFormat.SubjectPublicKeyInfo
)

mensaje = b'Ejemplo de uso de criptosistema RSA'

"""
    OAEP -> esquema de relleno para mejorar la seguridad del cifrado RSA.
         -> se utiliza para proteger contra ciertos tipos de ataques criptográficos.
    MGF1 -> algoritmo de generación de máscara que se utiliza internamente en OAEP.
         -> se utiliza para mezclar el mensaje antes de cifrarlo, proporcionando así aleatoriedad adicional y aumenta la seguridad del cifrado.
  SHA265 -> algoritmo hash, produce un resumen de 256 bits.     
"""
cifrado = public_key.encrypt(
    mensaje,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)

print('Mensaje cifrado: ' + str(cifrado))

descifrado = private_key.decrypt(
    cifrado, 
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)

print('Mensaje descifrado: ' + descifrado.decode('utf-8'))