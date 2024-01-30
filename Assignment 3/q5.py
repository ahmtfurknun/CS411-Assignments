import requests
import BitVector

API_URL = 'http://harpoon1.sabanciuniv.edu:9999'
my_id = 28315
def get_poly():
    endpoint = '{}/{}/{}'.format(API_URL, "poly", my_id )
    response = requests.get(endpoint)
    a = 0
    b = 0
    if response.ok:
        res = response.json()
        print(res)
        return res['a'], res['b']
    else:
        print(response.json())

def check_mult(c):
    #check result of part a
    endpoint = '{}/{}/{}/{}'.format(API_URL, "mult", my_id, c)
    response = requests.put(endpoint) 	
    print(response.json())

def check_inv(a_inv):
    #check result of part b
    response = requests.put('{}/{}/{}/{}'.format(API_URL, "inv", my_id, a_inv)) 
    print(response.json())

a, b = get_poly()
#{'a': '10010100', 'b': '11100000'}
##SOLUTION  

n = 8
poly = BitVector.BitVector(bitstring='111000011')
a = BitVector.BitVector(bitstring=a)
b = BitVector.BitVector(bitstring=b) 
#Part a
c = a.gf_multiply_modular(b, poly, n)
print("a(x) × b(x) = c(x) =", c)
#a(x) × b(x) = c(x) = 11011110
check_mult(c)


#Part b
a_inv = a.gf_MI(poly, n)
print("a^-1(x):", a_inv)
#a^-1(x): 00011011
check_inv(a_inv)

