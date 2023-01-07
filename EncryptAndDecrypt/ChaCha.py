from Crypto.Cipher import ChaCha20
from os import path


class ChaCha:
    def __init__(self, filename):
        self.key = 'KeyMustBe16ByteOR24ByteOR32Byte!'.encode('utf-8') #key in bytes (size of 32)
        self.filename = filename
        self.tuple = path.splitext(filename)
        self.name = self.tuple[0]
        self.ext = self.tuple[1]
    
    
    
    def cipher(self):
        archivo = None
        with open(self.filename, "rb") as File: #file type to encrypt and decrypt
            archivo = File.read()

        #print('***ChaCha20 Algorithm***\n')
        cipher = ChaCha20.new(key = self.key)
        self.Nonce = cipher.nonce
        ciphertext = cipher.encrypt(archivo)
        #print('\nChacha20 Encryption in Hexadecimal: ', ciphertext.hex())
        cipherFile = self.name + 'ChaCha20.bin'
        newFile = open(cipherFile,"wb")
        newFile.write(ciphertext) #ChaCha20 encrypted text in hex of the input file
        return ciphertext
        
    def decipher(self):
        with open(self.name + 'ChaCha20.bin', "rb") as File: #file type to encrypt and decrypt
            ciphertext = File.read()

        decipher = ChaCha20.new(key = self.key, nonce=self.Nonce)
        decrypted_file = decipher.decrypt(ciphertext)
        #print("\nThe decrypted message is: ", decrypted_file, '\n')

        descipherFile = self.name + '_ChaCha20_desc' + self.ext
        newFile = open(descipherFile,"wb")
        newFile.write(decrypted_file)

        return decrypted_file 
        
if __name__ == '__main__':
    cha = ChaCha('plain_text.txt')
    cha.cipher()
    cha.decipher()