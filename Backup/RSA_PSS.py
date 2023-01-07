from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import base64
import rsa

#Creacion de llaves en archivos pem
public_key, private_key = rsa.newkeys(1024)

# with open("public.pem", "wb") as f:
#   f.write(public_key.save_pkcs1("PEM"))
# with open("private.pem", "wb") as f:
#   f.write(private_key.save_pkcs1("PEM"))

archivo = None
with open("doc.pdf", "rb") as File: #file type to encrypt and decrypt
    archivo = File.read()

key = RSA.import_key(open('private.pem').read())
h = SHA256.new(archivo)
signature = pss.new(key).sign(h)
#------

key = RSA.import_key(open('public.pem').read())
h = SHA256.new(archivo)
verifier = pss.new(key)

try:
    verifier.verify(h, signature)
    print(base64.b64encode(signature))
    print ("The signature is authentic.")
   
except (ValueError, TypeError):
    print ("The signature is not authentic.")