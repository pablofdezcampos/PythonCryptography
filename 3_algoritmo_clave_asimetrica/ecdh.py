from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

private_key = parameters.generate_private_key()
public_key = private_key.public_key()

public_key_bytes = public_key.public_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PublicFormat.SubjectPublicKeyInfo 
)

received_public_key = serialization.load_pem_public_key(public_key_bytes, backend=default_backend())

shared_key = private_key.exchange(received_public_key)

print('Clave compartida: ' + shared_key.hex())