#!pip install cryptography

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import base64

#Proceso de firma
private_key = ec.generate_private_key(
    ec.SECT571K1() # Se supone que esto se cambia para que se prime o binary para este caso
    #https://neuromancer.sk/std/secg/sect571k1
)
with open("music.mp3", "rb") as imageFile: #file type to encrypt and decrypt
    archivo = imageFile.read()
#data = b"this is some data I'd like to sign"
signature = private_key.sign(
    archivo,
    ec.ECDSA(hashes.SHA256())
)

#Proceso comprobacion de firma
try:
    public_key = private_key.public_key()
    public_key.verify(signature, archivo, ec.ECDSA(hashes.SHA256()))
    #print(base64.b64encode(signature))
    #print("La firma es autentica")
except ValueError:
    print ("La firma no es autentica")