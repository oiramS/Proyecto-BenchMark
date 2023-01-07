from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

print('***AES CBC 256 Algorithm***\n')
BLOCK_SIZE = 16 # Bytes (256 bits)
key = 'KeyMustBe16ByteOR24ByteOR32Byte!' #256-bit/32-byte key for encryption
iv = bytes('abcdefghijklmnop', 'utf-8') #16-byte Initialization Vector
archivo = None

with open("plain_text.txt", "rb") as imageFile: #file type to encrypt and decrypt
    archivo = imageFile.read()

#Encrypt
cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, IV=iv)
ciphertext = cipher.encrypt(pad(archivo,BLOCK_SIZE))
#print('AES CBC Encrypted:', ciphertext.hex())

newFile = open("encrypted_file_CBC.txt","wb")
newFile.write(bytes(ciphertext.hex(), encoding='utf-8')) #AES CBC encrypted text in hex of the input file

#Decrypt
decipher = AES.new(key.encode('utf8'), AES.MODE_CBC, IV=iv)
decrypt = decipher.decrypt(ciphertext)
print(decrypt)
decrypted_file = unpad(decrypt, BLOCK_SIZE)
#print('AES CBC Decrypted Output: ', decrypted_file)

newFile = open("decrypted_file_CBC.txt","wb")
newFile.write(decrypted_file)