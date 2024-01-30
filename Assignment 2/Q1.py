#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import requests

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount
      
small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
                113]


API_URL = 'http://harpoon1.sabanciuniv.edu:9999/'

# Change your id here
my_id = 28315   

def getQ1():
    endpoint = '{}/{}/{}'.format(API_URL, "Q1", my_id )
    response = requests.get(endpoint)
    if response.ok:
        res = response.json()
        print(res)
        n, t = res['n'], res['t']
        return n,t
    else: print(response.json())

def checkQ1a(order):   #check your answer for Question 1 part a
    endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1a", my_id, order)
    response = requests.put(endpoint)
    print(response.json())

def checkQ1b(g):  #check your answer for Question 1 part b
    endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1b", my_id, g )#gH is generator of your subgroup
    response = requests.put(endpoint)#check result
    print(response.json())

def checkQ1c(gH):  #check your answer for Question 1 part c
    endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1c", my_id, gH )#gH is generator of your subgroup
    response = requests.put(endpoint)#check result
    print(response.json())

    
#Q1a
n, t = getQ1()
print("\nPhi(n):", phi(n))
checkQ1a(phi(n))

#Q1b
def is_generator(g, n):
    values = set()
    for i in range(2, n):
        generated = g ** i % n
        values.add(generated)
    return len(values) == phi(n)

for i in range(2, 100):
    if is_generator(i, n):
        print("\nSmallest generator:", i)
        break

checkQ1b(i)

#Q1c
def find_generator_with_order(n, order):
    g = 2
    while True:
        if g ** order % n == 1:
            return g
        g += 1

print("\nGenerator of Zt:", find_generator_with_order(n, t))
checkQ1c(find_generator_with_order(n, t))


'''
Phi(n): 462
Congrats!

Smallest generator: 3
Congrats!

Generator of Zt: 497
Congrats!
'''

