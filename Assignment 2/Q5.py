#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def LFSR(C, S):
    L = len(S)
    fb = 0
    out = S[L-1]
    for i in range(0,L):
        fb = fb^(S[i]&C[i+1])
    for i in range(L-1,0,-1):
        S[i] = S[i-1]

    S[0] = fb
    return out

def FindPeriod(s):
    n = len(s)
    for T in range(1,n+1):
        chck = 0
        for i in range(0,n-T-1):
            if (s[i] != s[i+T]):
                chck += 1
                break
        if chck == 0:
            break
    if T > n/2:
        return n
    else:
        return T     
    
def print_polynomial(coefficients):
    degree = len(coefficients) - 1
    polynomial = ""

    for i, coef in enumerate(reversed(coefficients)):
        if coef == 1:
            if degree - i == 0:
                polynomial += "1 +"
            elif degree - i == 1:
                polynomial += f"x + "
            else:
                polynomial += f"x^{degree - i} + "

    # Remove trailing '+'
    polynomial = polynomial.rstrip(" + ")

    return polynomial
    

def period(C):
    length = 256
    L = len(C)-1
    S = [0]*L

    for i in range(0,L):            # for random initial state
        S[i] = random.randint(0, 1)

    keystream = [0]*length
    for i in range(0,length):
        keystream[i] = LFSR(C, S)
            
    if FindPeriod(keystream) == 2**L - 1:
        print("Period for", print_polynomial(C)+":", FindPeriod(keystream), "=", 2**L - 1)
        print("Generates maximum period sequences.")
    else:
        print("Period for", print_polynomial(C)+":", FindPeriod(keystream), "<", 2**L - 1)
        print("Does not generate maximum period sequences.")
        
    print()
    

p1 = [1, 1, 0, 1, 0, 1, 0, 1]
period(p1)
#Period for x^7 + x^5 + x^3 + x + 1: 127 = 127
#Generates maximum period sequences.

p2 = [1, 0, 1, 0, 0, 1, 1]
period(p2)
#Period for x^6 + x^5 + x^2 + 1: 7 < 63
#Does not generate maximum period sequences.

p3 = [1, 1, 0, 1, 1, 1]
period(p3)
#Period for x^5 + x^4 + x^3 + x + 1: 31 = 31
#Generates maximum period sequences.

