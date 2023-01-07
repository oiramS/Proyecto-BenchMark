from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import rsa

def firmar_verificar(nombre):
  #public_key, private_key = rsa.newkeys(1024)
  with open(nombre, "rb") as imageFile: 
      archivo = imageFile.read()

  key = RSA.import_key(open('private.pem').read())
  h = SHA256.new(archivo)
  signature = pss.new(key).sign(h)

  key = RSA.import_key(open('public.pem').read())
  h = SHA256.new(archivo)
  verifier = pss.new(key)
  try:
      verifier.verify(h, signature)
      #print ("The signature is authentic.")
  except (ValueError, TypeError):
      print ("The signature is not authentic.")

#firmar_verificar("a.mp4")