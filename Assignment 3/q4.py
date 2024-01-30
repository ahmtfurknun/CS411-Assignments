def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

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
    
def factorize(n):
    upper_bound = int(n**0.5)+1
    for i in range(11, upper_bound, 2):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            continue
        elif n % i == 0:
            break
    p = i
    q = n/p
    return p, int(q)
    
def power(base, exponent, modulus=None):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus if modulus is not None else result * base
        base = (base * base) % modulus if modulus is not None else base * base
        exponent //= 2
    return result
    
N = 9244432371785620259
C = 655985469758642450
e = 2**16+1

p, q = factorize(N)

phi_n= (p-1) * (q-1)
d = modinv(e, phi_n)

x = power(C, d, N)
plaintext = x.to_bytes((x.bit_length() // 8 + 1 ), byteorder = 'big').decode('UTF-8')
print("p:", p)
print("q:", q)
print("Plaintext:", plaintext)
#p: 2485770689
#q: 3718940131
#Plaintext: Aloha!

