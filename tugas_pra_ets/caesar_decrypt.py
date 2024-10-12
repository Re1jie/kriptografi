def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def caesar_decrypt(input_file, key):
    result = ""
    for char in input_file:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

input_file = '/home/re1jie/ciphertext.txt'
output_file = '/home/re1jie/decrypted.txt'
key = 3
ciphertext = read_file(input_file)
plaintext = caesar_decrypt(ciphertext, key)
write_file(output_file, plaintext)
print("Decrypted")
