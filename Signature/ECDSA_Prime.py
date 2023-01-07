
#!pip install cryptography

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import base64

#Proceso de firma
private_key = ec.generate_private_key(
    ec.SECP521R1() # Se supone que esto se cambia para que se prime o binary para este caso
    #https://neuromancer.sk/std/secg/secp521r1
)
with open("doc.pdf", "rb") as imageFile: #file type to encrypt and decrypt
    archivo = imageFile.read()

signature = private_key.sign(
    archivo,
    ec.ECDSA(hashes.SHA256())
)

#Proceso comprobacion de firma
try:
    public_key = private_key.public_key()
    public_key.verify(signature, archivo, ec.ECDSA(hashes.SHA256()))
    print(base64.b64encode(signature))
    print("the signature is authentic.")
except ValueError:
    print ("the signature is not authentic.")