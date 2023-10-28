from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

mensaje = b'Ejemplo de mensaje a firmar con RSA'

"""
    PSS -> es un esquema de relleno utilizado en firmas digitales RSA.
        -> proporciona mayor aletoriedad al introducir elementos aleatorios en el proceso de firma.
        -> esta aletoriedad mejora la resitencia contra ciertos tipos de ataques.
    
    salt_length -> proporciona un valor que se agrega al mensaje antes de aplicar la función hash.
                -> esto introduce aleatoriedad adicional en el proceso de firma. 
                -> en este ejemplo establece la longitud de la sal al máximo permitido.  
"""

sign = private_key.sign(
    mensaje,
    padding.PSS(
        mgf = padding.MGF1(hashes.SHA256()),
        salt_length = padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

try:
    public_key.verify(
        sign,
        mensaje,
        padding.PSS(
           mgf = padding.MGF1(hashes.SHA256()),
           salt_length = padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print('Firma válida: El mensaje no ha sido moficado')
 
except Exception():
    print('Firma no válida: El mensaje ha sido modificado')        