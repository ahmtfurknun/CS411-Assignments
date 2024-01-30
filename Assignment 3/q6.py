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


a1 = 2700926558
b1 = 967358719
q1 = 3736942861

a2 = 1759062776
b2 = 1106845162
q2 = 3105999989

a3 = 2333074535
b3 = 2468838480
q3 = 2681377229

N = q1 * q2 * q3
N1 = q2 * q3
N2 = q1 * q3
N3 = q1 * q2

M1 = modinv(N1, q1)
M2 = modinv(N2, q2)
M3 = modinv(N3, q3)


x = (a1*b1*N1*M1 + a2*b2*N2*M2 + a3*b3*N3*M3) % N
print("Result R:", x)
print("R mod q1:", x % q1, "\t(a1 * b1) mod q1:", (a1*b1)%q1)
print("R mod q2:", x % q2, "\t(a2 * b2) mod q2:", (a2*b2)%q2)
print("R mod q3:", x % q3, "\t(a3 * b3) mod q3:", (a3*b3)%q3)
#Result: 17531516279242048504396112056
#R mod q1: 1643182479   (a1 * b1) mod q1: 1643182479
#R mod q2: 363289399    (a2 * b2) mod q2: 363289399
#R mod q3: 2376063578   (a3 * b3) mod q3: 2376063578

