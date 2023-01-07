from Hash import SHA2_384, SHA2_512, SHA3_384, SHA3_512
import matplotlib.pyplot as plt
import time

file = 'test/music.mp3' #test vector file

#SHA2-384
def fsha2_384():
    start = time.time()
    sha2_384 = SHA2_384.hash2_384(file)
    end = time.time()
    time_SHA2_384 = (end - start)*1000
    return time_SHA2_384

#SHA2-512
def fsha2_512():
    start = time.time()
    sha2_512 = SHA2_512.hash2_512(file)
    end = time.time()
    time_SHA2_512 = (end - start)*1000
    return time_SHA2_512
     

#SHA3-384
def fsha3_384():
    start = time.time()
    sha3_384 = SHA3_384.hash3_384(file)
    end = time.time()
    time_SHA3_384 = (end - start)*1000
    return time_SHA3_384

#SHA3-512
def fsha3_512():
    start = time.time()
    sha3_512 = SHA3_512.hash3_512(file)
    end = time.time()
    time_SHA3_512 = (end - start)*1000
    return time_SHA3_512

time_SHA2_384 = 0    
for i in range(10):
    time_SHA2_384 += fsha2_384()
time_SHA2_384 = time_SHA2_384 / 10

time_SHA2_512 = 0    
for i in range(10):
    time_SHA2_512 += fsha2_512()
time_SHA2_512 = time_SHA2_512 / 10

time_SHA3_384 = 0    
for i in range(10):
    time_SHA3_384 += fsha3_384()
time_SHA3_384 = time_SHA3_384 / 10

time_SHA3_512 = 0    
for i in range(10):
    time_SHA3_512 += fsha3_512()
time_SHA3_512 = time_SHA3_512 / 10


def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')

fig, ax = plt.subplots()
algoritmos = ['SHA2-384', 'SHA2-512', 'SHA3-384', 'SHA3-512']
tiempos = [time_SHA2_384, time_SHA2_512, time_SHA3_384, time_SHA3_512]
tiempos_labels = [round(time_SHA2_384,2), round(time_SHA2_512,2), round(time_SHA3_384,2), round(time_SHA3_512,2)]
bar_colors = ['red', 'blue', 'green', 'orange']

ax.bar(algoritmos, tiempos, color=bar_colors)
addlabels(algoritmos, tiempos_labels)
ax.set_ylabel('Time in milliseconds')
ax.set_title('Execution time of HASH algorithms')

plt.show()