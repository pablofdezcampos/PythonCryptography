from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

"""
    SECP384R1 -> representa la curva elíptica que se utiliza para generar el par de claves ECDSA
              -> es un estándar de la FIPS(Federal Information Processing Standards)
              -> conocido como P-256 en notación estándar
              -> Otras curvas elípticas, como SECP384R1 (P-384) y SECP521R1 (P-521): 
                    -> Ofrecen niveles de seguridad más altos.
                    -> Son más computacionalmente intensivas.
"""
private_key = ec.generate_private_key(ec.SECP384R1(), backend = default_backend())
public_key = private_key.public_key()

mensaje = b'Ejemplo de mensaje a firmar con ECDSA'

sign = private_key.sign(
    mensaje,
    ec.ECDSA(hashes.SHA256())
)

try:
    public_key.verify(sign, mensaje, ec.ECDSA(hashes.SHA256()))
    print('Firma válida: El mensaje no ha sido moficado')
    
except Exception():
    print('Firma no válida: El mensaje ha sido modificado')