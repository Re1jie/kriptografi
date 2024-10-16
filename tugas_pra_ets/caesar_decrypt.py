alph_lwr = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_upr = [chr(i) for i in range(ord('A'), ord('Z')+1)]

def dekripsi(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char in alph_lwr:
            temp = alph_lwr.index(char)
            indeks = (temp - key) % 26
            result += alph_lwr[indeks]
        elif char in alph_upr:
            temp = alph_upr.index(char)
            indeks = (temp - key) % 26
            result += alph_upr[indeks]
        else:
            result += char
    return result

ciphertext = "khoor zruog"
key = 3

plaintext= dekripsi(ciphertext, key)
print(plaintext)