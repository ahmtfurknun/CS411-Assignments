from Crypto.Hash import SHAKE128

k0 = 8
k1 = 128

def RSA_OAEP_Enc(m, e, N, R):
    k = N.bit_length()-2
    m0k1 = m << k1
    shake = SHAKE128.new(R.to_bytes(k0//8, byteorder='big'))
    GR =  shake.read((k-k0)//8)
    m0k1GR = m0k1 ^ int.from_bytes(GR, byteorder='big')
    shake = SHAKE128.new(m0k1GR.to_bytes((m0k1GR.bit_length()+7)//8, byteorder='big'))
    Hm0k1GR =  shake.read(k0//8)
    RHm0k1GR = R ^ int.from_bytes(Hm0k1GR, byteorder='big')
    m_ = (m0k1GR << k0) + RHm0k1GR
    c = pow(m_, e, N)
    return c


C = 15563317436145196345966012870951355467518223110264667537181074973436065350566
e = 65537
N = 73420032891236901695050447655500861343824713605141822866885089621205131680183
correct_pin_found = False
pin = 0
R = 0

#check every pin
for p in range(1000, 10000):
    #check every random number r
    for r in range(256):
        #if encryprion of plaintext is ciphertet is same, we found
        if RSA_OAEP_Enc(p, e, N, r) == C:
            pin = p
            R = r
            correct_pin_found = True
            break

    if correct_pin_found:
        break

print("Pin:", pin)
print("R:", R)

