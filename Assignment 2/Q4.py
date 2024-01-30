#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

def solution(a, b, n):
    d = gcd(a, n)
    if d == 1:
        x = (modinv(a, n) * b) % n
        print("Solution for x:", x)
    elif b % d != 0:
        print("No solution exists.")
    else:
        x = modinv(a//d, n//d) * (b//d) % (n//d)
        for i in range(d):
            solution = x + i*n/d
            print("Solution "+str(i+1)+" for x:", int(solution))
            
n = 2163549842134198432168413248765413213216846313201654681321666
a = 790561357610948121359486508174511392048190453149805781203471
b = 789213546531316846789795646513847987986321321489798756453122

solution(a, b, n)
#Solution for x: 1115636343148004398322135138661008357945126147114770093414826
print()

n = 3213658549865135168979651321658479846132113478463213516854666
a = 789651315469879651321564984635213654984153213216584984653138
b = 798796513213549846121654984652134168796513216854984321354987

solution(a, b, n)
#No solution exists.
print()

n = 5465132165884684652134189498513211231584651321849654897498222
a = 654652132165498465231321654946513216854984652132165849651312
b = 987965132135498749652131684984653216587986515149879613516844

solution(a, b, n)
#Solution 1 for x: 1840451085636978953532199331848468040344984676540251260321792
#Solution 2 for x: 4573017168579321270146013347041736918185381188858187729600512
print()

n = 6285867509106222295001894542787657383846562979010156750642244
a = 798442746309714903987853299207137826650460450190001016593820
b = 263077027284763417836483408268884721142505761791336585685868

solution(a, b, n)
#Solution 1 for x: 120574576795431471255391068881120779719031331072977934483456
#Solution 2 for x: 1692041454071987087403821515865499722587517050936117136719872
#Solution 3 for x: 3263508331348542592048525970196762957777411407557448809054208
#Solution 4 for x: 4834975208625098096693230424528026192967305764178780481388544
