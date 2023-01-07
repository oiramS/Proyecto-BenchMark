from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec 

def firmar_verificar(nombre):
    private_key = ec.generate_private_key(
        ec.SECT571K1() 
    )
    with open(nombre, "rb") as imageFile: 
        archivo = imageFile.read()
    signature = private_key.sign(
        archivo,
        ec.ECDSA(hashes.SHA256())
    )
    try:
        public_key = private_key.public_key()
        public_key.verify(signature, archivo, ec.ECDSA(hashes.SHA256()))
        #print("La firma es autentica")
    except (Exception):
        print ("La firma no es autentica")
#firmar_verificar("a.mp4")
