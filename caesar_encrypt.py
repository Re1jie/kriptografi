def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

# Contoh penggunaan dengan file
input_file = '/home/re1jie/plaintext.txt'
output_file = '/home/re1jie/ciphertext.txt'
key = 3

# Membaca isi file
plaintext = read_file(input_file)

# Mengenkripsi teks
ciphertext = caesar_encrypt(plaintext, key)

# Menyimpan hasil enkripsi ke file baru
write_file(output_file, ciphertext)
print("Encrypted")
