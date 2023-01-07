from Crypto.Hash import SHA384


def hash2_384(file_name):
    hash2_384 = SHA384.new()
    
    with open(file_name, 'rb') as file:
        for i in file.readlines():
            hash2_384.update(i)    
    
    return hash2_384.hexdigest()

#print(hash2_384('music.mp3'))
