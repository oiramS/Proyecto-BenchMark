from Crypto.Hash import SHA3_512


def hash3_512(file_name):
    hash3_512 = SHA3_512.new()
    
    with open(file_name, 'rb') as file:
        for i in file.readlines():
            hash3_512.update(i)    
    
    return hash3_512.hexdigest()

#print(hash3_512('imagen.jpg'))