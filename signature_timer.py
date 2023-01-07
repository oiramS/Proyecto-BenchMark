from Signature import rsa_pss, ecdsa_prime_field, ecdsa_binary_field
import matplotlib.pyplot as plt
import time

file ='test/music.mp3' #test vector file

#RSA-PSS
def fRSA_PSS():
    start = time.time()
    RSA_PSS = rsa_pss.firmar_verificar(file)
    end = time.time()
    time_RSAPSS = (end - start)*1000
    return time_RSAPSS 

#ECDSA-PRIME
def fECDSA_PRIME():
    start = time.time()
    ECDSA_PRIME = ecdsa_prime_field.firmar_verificar(file)
    end = time.time()
    time_ECDSA_PRIME = (end - start)*1000
    return time_ECDSA_PRIME

#ECDSA-BYNARY
def fECDSA_BYNARY():
    start = time.time()
    ECDSA_BINARY = ecdsa_binary_field.firmar_verificar(file)
    end = time.time()
    time_ECDSA_BINARY = (end - start)*1000
    return time_ECDSA_BINARY

time_RSA_PSS = 0    
for i in range(10):
    time_RSA_PSS += fRSA_PSS()
time_RSA_PSS = time_RSA_PSS / 10

time_ECDSA_PRIME = 0    
for i in range(10):
    time_ECDSA_PRIME += fECDSA_PRIME()
time_ECDSA_PRIME = time_ECDSA_PRIME / 10

time_ECDSA_BINARY = 0    
for i in range(10):
    time_ECDSA_BINARY += fECDSA_BYNARY()
time_ECDSA_BINARY = time_ECDSA_BINARY / 10

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')

fig, ax = plt.subplots()
algoritmos = ['RSA PSS', 'ECDSA PRIME', 'ECDSA BINARY']
tiempos = [time_RSA_PSS, time_ECDSA_PRIME, time_ECDSA_BINARY]
tiempos_labels = [round(time_RSA_PSS,2), round(time_ECDSA_PRIME,2), round(time_ECDSA_BINARY,2)]
bar_colors = ['red', 'blue', 'green']

ax.bar(algoritmos, tiempos, color=bar_colors)
addlabels(algoritmos, tiempos_labels)
ax.set_ylabel('Time in milliseconds')
ax.set_title('Execution time of signature algorithms')

plt.show()