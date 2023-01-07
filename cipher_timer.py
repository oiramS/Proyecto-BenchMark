from EncryptAndDecrypt import AES_ECB, AES_CBC, ChaCha, RSA_OAEP
import matplotlib.pyplot as plt
import time

file = 'test/plain_text.txt' #test vector file

aes_cbc = AES_CBC.AES_CBC(file)
aes_ecb = AES_ECB.AES_ECB(file)
cha = ChaCha.ChaCha(file)
rsa = RSA_OAEP.RSA_OAEP(file)
#AES_ECB
def fAES_ECB():
    start = time.time()
    aes_ecb.cipher()
    end = time.time()
    time_AES_ECB_cipher = (end - start)*1000
    
    start = time.time()
    aes_ecb.decipher()
    end = time.time()
    time_AES_ECB_decipher = (end - start)*1000
    
    return time_AES_ECB_cipher, time_AES_ECB_decipher

#AES_CBC
def fAES_CBC():
    start = time.time()
    aes_cbc.cipher()
    end = time.time()
    time_AES_CBC_cipher = (end - start)*1000
    
    start = time.time()
    aes_cbc.decipher()
    end = time.time()
    time_AES_CBC_decipher = (end - start)*1000
    
    return time_AES_CBC_cipher, time_AES_CBC_decipher

#ChaCha20
def fChaCha20():
    start = time.time()
    cha.cipher()
    end = time.time()
    time_ChaCha20_cipher = (end - start)*1000
    
    start = time.time()
    cha.decipher()
    end = time.time()
    time_ChaCha20_decipher = (end - start)*1000
    
    return time_ChaCha20_cipher, time_ChaCha20_decipher

#RSA_OAEP
def fRSA_OAEP():
    start = time.time()
    rsa.cipher()
    end = time.time()
    time_RSA_OAEP_cipher = (end - start)*1000
    
    start = time.time()
    rsa.decipher()
    end = time.time()
    time_RSA_OAEP_decipher = (end - start)*1000
    
    return time_RSA_OAEP_cipher, time_RSA_OAEP_decipher


time_AES_ECB_cip = 0
time_AES_ECB_des = 0     
for i in range(10):
    res = fAES_ECB()
    time_AES_ECB_cip += res[0]
    time_AES_ECB_des += res[1]
time_AES_ECB_cip = time_AES_ECB_cip / 10
time_AES_ECB_des = time_AES_ECB_des / 10


time_AES_CBC_cip = 0
time_AES_CBC_des = 0 
for i in range(10):
    res = fAES_CBC()
    time_AES_CBC_cip += res[0]
    time_AES_CBC_des += res[1]
time_AES_CBC_cip = time_AES_CBC_cip / 10
time_AES_CBC_des = time_AES_CBC_des / 10

time_ChaCha20_cip = 0
time_ChaCha20_des = 0      
for i in range(10):
    res = fChaCha20()
    time_ChaCha20_cip += res[0]
    time_ChaCha20_des += res[1] 
time_ChaCha20_cip = time_ChaCha20_cip / 10
time_ChaCha20_des = time_ChaCha20_des / 10

time_RSA_OAEP_cip = 0
time_RSA_OAEP_des = 0  
if (file.endswith('.txt')):
    for i in range(10):
        res = fRSA_OAEP()
        time_RSA_OAEP_cip += res[0]
        time_RSA_OAEP_des += res[1]
    time_RSA_OAEP_cip = time_RSA_OAEP_cip / 10
    time_RSA_OAEP_des = time_RSA_OAEP_des / 10
    

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


fig, ax = plt.subplots()
algoritmos = ['AES-ECB', 'AES-CBC', 'ChaCha20', 'RSA-OAEP']
tiempos = [time_AES_ECB_cip, time_AES_CBC_cip, time_ChaCha20_cip, time_RSA_OAEP_cip]
tiempos_labels = [round(time_AES_ECB_cip,2), round(time_AES_CBC_cip,2), round(time_ChaCha20_cip,2), round(time_RSA_OAEP_cip,2)]
bar_colors = ['red', 'blue', 'green', 'orange']

ax.bar(algoritmos, tiempos, color=bar_colors)
addlabels(algoritmos, tiempos_labels)
ax.set_ylabel('Time in milliseconds')
ax.set_title('Execution time of the encryption algorithms')
plt.show()

fig, ax = plt.subplots()
tiempos2 = [time_AES_ECB_des, time_AES_CBC_des, time_ChaCha20_des, time_RSA_OAEP_des]
tiempos_labels2 = [round(time_AES_ECB_des,2), round(time_AES_CBC_des,2), round(time_ChaCha20_des,2), round(time_RSA_OAEP_des,2)]
bar_colors = ['red', 'blue', 'green', 'orange']

ax.bar(algoritmos, tiempos2, color=bar_colors)
addlabels(algoritmos, tiempos_labels2)
ax.set_ylabel('Time in milliseconds')
ax.set_title('Execution time of the decryption algorithms')
plt.show()