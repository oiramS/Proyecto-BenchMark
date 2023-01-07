from Crypto.Cipher import ChaCha20

archivo = None
key = 'KeyMustBe16ByteOR24ByteOR32Byte!'.encode('utf-8') #key in bytes (size of 32)
with open("doc.pdf", "rb") as File: #file type to encrypt and decrypt
    archivo = File.read()

print('***ChaCha20 Algorithm***\n')
cipher = ChaCha20.new(key=key)
Nonce = cipher.nonce
ciphertext = cipher.encrypt(archivo)
#print('\nChacha20 Encryption in Hexadecimal: ', ciphertext.hex())

newFile = open("encrypted_file_ChaCha.txt","wb")
newFile.write(bytes(ciphertext.hex(), encoding='utf-8')) #ChaCha20 encrypted text in hex of the input file

decipher = ChaCha20.new(key=key, nonce=Nonce)
decrypted_file = decipher.decrypt(ciphertext)
#print("\nThe decrypted message is: ", decrypted_file, '\n')

newFile = open("decrypted_file_ChaCha.pdf","wb")
newFile.write(decrypted_file)