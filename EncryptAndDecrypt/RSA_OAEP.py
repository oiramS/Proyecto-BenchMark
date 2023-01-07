#pip install pycryptodome
#pip install rsa
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import rsa
from os import path

class RSA_OAEP:
    def __init__(self, filename):
        self.filename = filename
        self.tuple = path.splitext(filename)
        self.name = self.tuple[0]
        self.ext = self.tuple[1]
        public_key, private_key = rsa.newkeys(1024)
        with open("test/public.pem", "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))
        with open("test/private.pem", "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))
        
    def cipher(self):
        archivo = None
        with open(self.filename, "rb") as File: #file type to encrypt and decrypt
            archivo = File.read()
        key = RSA.importKey(open('test/public.pem').read())
        cipher = PKCS1_OAEP.new(key)
        ciphertext = cipher.encrypt(archivo)
        cipherFile = self.name + 'RSA_OAEP.bin'
        newFile = open(cipherFile,"wb")
        newFile.write(ciphertext) #ChaCha20 encrypted text in hex of the input file
        return ciphertext
    
    def decipher(self):
        with open(self.name + 'RSA_OAEP.bin', "rb") as File: #file type to encrypt and decrypt
            ciphertext = File.read()
        key = RSA.importKey(open('test/private.pem').read())
        cipher = PKCS1_OAEP.new(key)
        decrypt_message = cipher.decrypt(ciphertext)
        descipherFile = self.name + '_RSA_OAEP_desc' + self.ext
        newFile = open(descipherFile,"wb")
        newFile.write(decrypt_message)
        return decrypt_message
           
if __name__ == '__main__':
    rsa = RSA_OAEP('plain_text.txt')
    rsa.cipher()
    rsa.decipher()