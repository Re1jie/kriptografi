alph_lwr = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_upr = [chr(i) for i in range(ord('A'), ord('Z')+1)]

def read_file(filetext):
    with open(filetext, 'r') as file:
        return file.read()

def write_file(filetext, isitext):
    with open(filetext, 'w') as file:
        file.write(isitext)

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

input_file = '/home/re1jie/kriptografi/ciphertext.txt'
output_file = '/home/re1jie/kriptografi/plaintext_i.txt'
key = 3
ciphertext = read_file(input_file)
plaintext= dekripsi(ciphertext, key)
write_file(output_file, plaintext)
print("pesan telah ter dekripsi di path : "+output_file)