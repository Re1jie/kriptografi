# Method untuk menghitung invers modular
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

# Method untuk mendekripsi ciphertext
def decrypt(ciphertext, d, N):
    decryptedtext = []
    for char in ciphertext:
        if char.isdigit():  # Jika elemen adalah angka
            decrypted_value = pow(int(char), d, N)
            decrypted_char = chr((decrypted_value % 26) + ord('a'))
            decryptedtext.append(decrypted_char)
        else:
            decryptedtext.append(char)
    return ''.join(decryptedtext)

if __name__ == "__main__":
    p = int(input('Masukkan p : '))
    q = int(input('Masukkan q : '))

    N = p * q
    phi_N = (p - 1) * (q - 1)

    with open("key.txt", "r") as file:
        e, N_from_file = map(int, file.read().split(','))
        if N_from_file != N:
            print("Nilai N tidak cocok dengan kunci.")
            exit()

    d = mod_inverse(e, phi_N)

    with open("ciphertext.txt", "r") as file:
        ciphertext = file.read().split()

    decryptedtext = decrypt(ciphertext, d, N)

    # Output
    print(f"Private key: ({d},{N})")
    print(f"Decryptedtext: {decryptedtext}")
