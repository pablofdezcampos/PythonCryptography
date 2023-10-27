from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())
public_key = private_key.public_key()

# Mensaje a firmar
mensaje = b"Ejemplo de mensaje con firma DSA"

#Firmar el mensaje
sign = private_key.sign(mensaje, hashes.SHA256())

#Verificar la firma
try:
    public_key.verify(sign, mensaje, hashes.SHA256())
    print("Firma válida: El mensaje no ha sido modificado.")
except Exception:
    print("Firma no válida: El mensaje ha sido modificado.")