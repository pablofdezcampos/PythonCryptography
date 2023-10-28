"""
    EJEMPLO DE USA DSA PARA VALIDAR LA FIRMA
"""
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key = DSA.generate(2048)

mensaje = b'Ejemplo de firma con DSA'

#Crea el objeto firma
sign_object = SHA256.new(mensaje)

#fips-186-3 -> es un estándar del gobierno de EE. UU. para la generación y verificación de firmas digitales.
#DSS -> es utilizado para en este caso firmar datos, aporta funcionalidades a DSA
signer = DSS.new(key, 'fips-186-3')

#Firmar el mensaje
sign = signer.sign(sign_object)

#Creación del objeto verificador
#DSS -> utilizado en este caso para verificar
verifier = DSS.new(key, 'fips-186-3')

try:
    
    verifier.verify(sign, sign_object)
    print('Firma válida: El mensaje no ha sido modificado')

except ValueError:
    print('Firma no válida: El mensaje ha sido modificado')