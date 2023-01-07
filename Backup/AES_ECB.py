from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

print('***AES ECB 256 Algorithm***\n')
BLOCK_SIZE = 16 # Bytes (256 bits)
key = 'KeyMustBe16ByteOR24ByteOR32Byte!' #256-bit/32-byte key for encryption
archivo = None

with open("doc.pdf", "rb") as imageFile: #file type to encrypt and decrypt
    archivo = imageFile.read()

#Encrypt
cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(archivo,BLOCK_SIZE))
#print('AES ECB Encrypted:', ciphertext.hex())

newFile = open("encrypted_file_ECB.txt","wb")
newFile.write(bytes(ciphertext.hex(), encoding='utf-8')) #AES ECB encrypted text in hex of the input file

#Decrypt
decrypt = cipher.decrypt(ciphertext)
decrypted_file = unpad(decrypt, BLOCK_SIZE)
#print('AES ECB Decrypted Output: ', decrypted_file)

newFile = open("decrypted_file_ECB.pdf","wb")
newFile.write(decrypted_file)