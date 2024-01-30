import requests


API_URL = 'http://harpoon1.sabanciuniv.edu:9999'
my_id = 28315

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
def RSA_Oracle_Get():
    response = requests.get('{}/{}/{}'.format(API_URL, "RSA_Oracle", my_id))
    c, N, e = 0,0,0 
    if response.ok:
        res = response.json()
        print(res)
        return res['c'], res['N'], res['e']
    else:
        print(response.json())

def RSA_Oracle_Query(c_):
    response = requests.get('{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_Query", my_id, c_)) 
    print(response.json())
    m_= ""
    if response.ok: 
        m_ = (response.json()['m_'])
    else: 
        print(response)
    return m_

def RSA_Oracle_Checker(m):
    response = requests.put('{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_Checker", my_id, m))
    print(response.json())
    
def power(base, exponent, modulus=None):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus if modulus is not None else result * base
        base = (base * base) % modulus if modulus is not None else base * base
        exponent //= 2
    return result

c, N, e = RSA_Oracle_Get()

#random number r
r = 3

#C_ ≡ C · r^e (mod N )
c_ = (power(r, e, N) * c) % N 

#m_ should be m_ ≡ M · r (mod N) 
m_ = RSA_Oracle_Query(c_) 

#m should be M ≡ m_ · r^-1 (mod N) 
m = (m_ * modinv(r, N)) % N 

print()
print("Decrypted m:", m)
message = m.to_bytes((m.bit_length() // 8 + 1), byteorder="big").decode()
print("Decoded m:", message)
RSA_Oracle_Checker(message)

