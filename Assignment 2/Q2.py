#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
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


API_URL = 'http://harpoon1.sabanciuniv.edu:9999/'

# Change your id here
my_id = 28315   


def getQ2():
    endpoint = '{}/{}/{}'.format(API_URL, "Q2", my_id )
    response = requests.get(endpoint)
    if response.ok:
        res = response.json()
        e, cipher = res['e'], res['cipher']
        return e, cipher
    else:  print(response.json())

def checkQ2(ptext):  #check your answer for Question 2
    response = requests.put('{}/{}'.format(API_URL, "checkQ2"), json = {"ID": my_id, "msg":ptext})
    print(response.json())

def power(base, exponent, modulus=None):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus if modulus is not None else result * base
        base = (base * base) % modulus if modulus is not None else base * base
        exponent //= 2
    return result

e, c = getQ2()
p =163812632438116402334651955238877888051471698595800699322979615035703105353498598900017754479082745390305183480326386193928762023006697325502630355995540302095536983747674239699082775937971908945314983176639634719523082664655125286220339981282043117576435108592265744474672826334454420325847233209118053745479
q =167991311406281829893277907517380926743297770437237817698088843729837413680407121035993724942424328049100226903066919418963576739130754375674323262394889417412537943169688299724092631996519692955388293697048331540030669504591419100438660952486903606581569836090930608369486871356825028654569386086674053846173

n = p * q

phi_n = (p-1) * (q-1)

d = modinv(e, phi_n)
m = power(c, d, n)

m_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
decoded_message = m_bytes.decode("utf-8")
print(decoded_message)
checkQ2(decoded_message)

'''
I think I have 926 unread e-mails. Is that a lot?
Congrats!
'''

