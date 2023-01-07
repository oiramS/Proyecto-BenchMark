#pip install pycryptodome
#pip install rsa

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import b64decode,b64encode
import rsa

#Creacion de llaves en archivos pem
public_key, private_key = rsa.newkeys(1024)

with open("public.pem", "wb") as f:
  f.write(public_key.save_pkcs1("PEM"))
with open("private.pem", "wb") as f:
  f.write(private_key.save_pkcs1("PEM"))

#Proceso de encriptación 
archivo = None
with open("plain_text.txt", "rb") as File: #file type to encrypt and decrypt
    archivo = File.read()

key = RSA.importKey(open('public.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(archivo)
print('ciphertext is: ', ciphertext.hex())

#Proceso de desencriptación
key = RSA.importKey(open('private.pem').read())
cipher = PKCS1_OAEP.new(key)
message = cipher.decrypt(ciphertext)
print('\n', message)
