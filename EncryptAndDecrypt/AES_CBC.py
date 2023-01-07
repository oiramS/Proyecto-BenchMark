from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import os

class AES_CBC:
    def __init__(self, filename):
        self.BLOCK_SIZE = 16 # Bytes (256 bits)
        self.key = 'KeyMustBe16ByteOR24ByteOR32Byte!' #256-bit/32-byte key for encryption
        self.iv = bytes('abcdefghijklmnop', 'utf-8')
        self.filename = filename
        self.tuple = os.path.splitext(filename)
        self.name = self.tuple[0]
        self.ext = self.tuple[1]
        
    def cipher(self):
        #print('***AES CBC 256 Algorithm***\n')
        #16-byte Initialization Vector
        archivo = None

        with open(self.filename, "rb") as file: #file type to encrypt and decrypt
            archivo = file.read()

        #Encrypt
        cipher = AES.new(self.key.encode('utf8'), AES.MODE_CBC, IV = self.iv)
        self.ciphertext = cipher.encrypt(pad(archivo, self.BLOCK_SIZE))
        #print('AES CBC Encrypted:', ciphertext.hex())
        cipherFile = self.name + '_AES_CBC.bin'
        newFile = open(cipherFile,"wb")
        newFile.write(self.ciphertext) #AES CBC encrypted text in hex of the input file
        
        return self.ciphertext


    def decipher(self):
        #Decrypt
        ciphertext = None
        with open(self.name + '_AES_CBC.bin', "rb") as file: #file type to encrypt and decrypt
            ciphertext = file.read()
            
        decipher = AES.new(self.key.encode('utf8'), AES.MODE_CBC, IV = self.iv)
        decrypt = decipher.decrypt(ciphertext)
        decrypted_file = unpad(decrypt, self.BLOCK_SIZE)
        #print('AES CBC Decrypted Output: ', decrypted_file)
        descipherFile = self.name + '_AES_CBC_desc' + self.ext
        newFile = open(descipherFile,"wb")
        newFile.write(decrypted_file)
        return decrypted_file


if __name__ == '__main__':
    aes = AES_CBC('plain_text.txt')
    aes.cipher()
    aes.decipher()
    