from Crypto.Hash import SHA512


def hash2_512(file_name):
    hash2_512 = SHA512.new()
    
    with open(file_name, 'rb') as file:
        for i in file.readlines():
            hash2_512.update(i)    
    
    return hash2_512.hexdigest()

#print(hash2_512('imagen.jpg'))