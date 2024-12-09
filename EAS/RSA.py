from math import gcd

# Parameter RSA
plaintext = str(input('Masukkan plaintext : '))
p = int(input('Masukkan p : '))
q = int(input('Masukkan q : '))
N = p * q
phi_N = (p - 1) * (q - 1)

# Menghitung e
def FPB(phi_N):
    for e in range(2, phi_N):
        if gcd(e, phi_N) == 1:
            return e
    return None

e = FPB(phi_N)

# Menghitung d dengan Extended Euclidean
def mod_inverse(e, phi_N):
    t1, t2 = 0, 1
    r1, r2 = phi_N, e
    while r2 != 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        t1, t2 = t2, t1 - q * t2
    if t1 < 0:
        t1 += phi_N
    return t1

d = mod_inverse(e, phi_N)

# Method untuk mengenkripsi plaintext
def encrypt(plaintext, e, N):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            a = ord(char.lower()) - ord('a')
            encrypted_value = pow(a, e) % N
            ciphertext.append(encrypted_value)
        else:
            ciphertext.append(char)
    return ciphertext

# Method untuk mendekripsi ciphertext
def decrypt(ciphertext, d, N):
    decryptedtext = []
    for char in ciphertext:
        if isinstance(char, int):
            decrypted_value = pow(char, d) % N
            decrypted_char = chr((decrypted_value % 26) + ord('a'))
            decryptedtext.append(decrypted_char)
        else:
            decryptedtext.append(char)
    return ''.join(decryptedtext)

# Enkripsi dan Dekripsi
ciphertext = encrypt(plaintext, e, N)
decryptedtext = decrypt(ciphertext, d, N)

ciphertext = encrypt(plaintext, e, N)
decryptedtext = decrypt(ciphertext, d, N)

# Konversi ciphertext menjadi string
ciphertext_str = ' '.join(str(c) if isinstance(c, int) else c for c in ciphertext)

# Output
print(f"Public key: ({e},{N})")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext_str}")
print(f"Private key: ({d},{N})")
print(f"Decryptedtext: {decryptedtext}")
