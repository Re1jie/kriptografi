from math import gcd

# Menghitung FPB untuk menentukan nilai e
def FPB(phi_N):
    for e in range(2, phi_N):
        if gcd(e, phi_N) == 1:
            return e
    return None

# Method untuk mengenkripsi plaintext
def encrypt(plaintext, e, N):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            a = ord(char.lower()) - ord('a')
            encrypted_value = pow(a, e, N)
            ciphertext.append(encrypted_value)
        else:
            ciphertext.append(char)
    return ciphertext

if __name__ == "__main__":
    plaintext = str(input('Masukkan plaintext : '))
    p = int(input('Masukkan p : '))
    q = int(input('Masukkan q : '))

    N = p * q
    phi_N = (p - 1) * (q - 1)
    e = FPB(phi_N)

    if e is None:
        print("Tidak dapat menemukan e yang memenuhi syarat.")
        exit()

    ciphertext = encrypt(plaintext, e, N)

    # Konversi ciphertext menjadi string
    ciphertext_str = ' '.join(str(c) if isinstance(c, int) else c for c in ciphertext)

    # Output
    print(f"Public key: ({e},{N})")
    print(f"Ciphertext: {ciphertext_str}")

    # Simpan ke file
    with open("ciphertext.txt", "w") as file:
        file.write(ciphertext_str)
    with open("key.txt", "w") as file:
        file.write(f"{e},{N}")
