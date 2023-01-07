from Crypto.Hash import SHA3_384


def hash3_384(file_name):
    hash3_384 = SHA3_384.new()
    
    with open(file_name, 'rb') as file:
        for i in file.readlines():
            hash3_384.update(i)    
    
    return hash3_384.hexdigest()

#print(hash3_384('imagen.jpg'))
