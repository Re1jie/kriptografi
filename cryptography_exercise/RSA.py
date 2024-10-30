p = 2
q = 7
product = p * q
func = (p-1)*(q-1)
e = 0
def gcd(a, b):
    if(b==0):
        return abs(a)
    else:
        return gcd(b, a % b)
for i in range(2, func):
    if gcd(i, func) == 1 and gcd(i, product) == 1:
        e = i
        break
    
print("public key : (", e,",", product,")")
# plaintext = "hello"
# alph = [chr(i) for i in range(ord('a'), ord('z')+1)]