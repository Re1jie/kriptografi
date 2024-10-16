alph_lwr = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_upr = [chr(i) for i in range(ord('A'), ord('Z')+1)]

def enkripsi(plaintext, key):
    result = ""
    for char in plaintext:
        if char in alph_lwr:
            temp = alph_lwr.index(char)
            indeks = (temp + key) % 26
            result += alph_lwr[indeks]
        elif char in alph_upr:
            temp = alph_upr.index(char)
            indeks = (temp + key) % 26
            result += alph_upr[indeks]
        else:
            result += char
    return result

plaintext = "hello world"
key = 3
ciphertext = enkripsi(plaintext, key)
print(ciphertext)