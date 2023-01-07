# 🔒 Cryptography Project: Benchmarks

This project uses various cryptography libraries to implement a benchmark fo the following algorithms:

- Cipher and decipher
  - AES-CBC
  - AES-ECB
  - ChaCha20
  - RSA-OAEP
- Hashing
  - SHA-2 384
  - sHA-2 512
  - SHA-3 384
  - SHA-3 512
- Signature
  - ECDSA Binary Field
  - ECDSA Prime Field
  - RSA-PSS

## 📋 Requirements

- Python 3.6 or higher
- matplotlib
- Crypto
- pycryptodome
- cryptography
- rsa

## 💾 Installation

1. Install Python 3.6 or higher if it is not already installed on your system.
2. Install the required libraries using pip:

```bash
pip install crypto pycryptodome cryptography rsa

```

## 🚀 Usage

```bash
# returns the cipher and decipher algorithms benchmark graphics (the decipher graphics are shown after closing the cipher ones)
python cipher_timer.py

# returns the hashing algorithms benchmark graphics
python hash_timer.py


# returns the signature algorithms benchmark graphics
python signature_timer.py

```

To change the testing vector, change the following variable inside the desired benchmark. Example:\
Inside `hash.py` change the `file` variable:

```python
file ='test/plaint_text.txt'

```

to

```python
file ='test/music.mp3'

```

to do the benchmark over the mp3 file.

## 🤝 Authors

Domínguez Fuentes Luis Mario\
Nicolas Marin Brian Geovanny\
Rosales Mendoza José Francisco\

## 📜 License

[MIT](https://choosealicense.com/licenses/mit/)
