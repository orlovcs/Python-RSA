import math, random

# Make sure both primes just in case 
def phi(primeone, primetwo):
    if primeCheck(primeone) and primeCheck(primetwo):
        return (primeone - 1) * (primetwo - 1)

# Reads in ints     
def primeCheck(prime):
    if prime > 1:
        for i in range(2,prime):
            if (prime % i == 0):
                return False
        else:
            return True
    else:
        return False

def privatekey(e, p, q):
    phiN = phi(p,q)
    i = 0
    f = 0
    #ed===1 mod phiN
    for i in range(1,phiN):
        if (1==(e*i)%phiN):
            break
    # check this after d is found then offer variations 1<d<phiN
    if (1<i<phiN):
      print("Your private key d is: ",i)
      return i
    else:
      while not (1<i<phiN):
        for f in range(0,(random.randint(0, 9))):
          if (1==(e*f)%phiN):
            break
      print("Your private key d is: ",f)
      return f
   # 37, 107, 997
   # 3, 107, 101


def encryptor():
    #0 <= C < pq and C === M**e (mod pq).
    #ask for string then deconstruct into encruypted chars and into string array 
    return 4

def decryptor():
    #R === C**d (mod pq) with 0 <= R < pq.
#ask for string then deconstruct into encruypted chars and into string array 
    return 4


def publickeys():
    p = input("Enter a large distinct prime p: ")
    q = input("Enter a large distinct prime q: ")
    p = int(p)
    q = int(q)
    while p==q or not primeCheck(p) or not primeCheck(q) or p <=100 or q <= 100:
        if p==q:
            print("Error: numbers are identical")
        if not primeCheck(p):
            print("Error: p is not a prime")
        if not primeCheck(q):
            print("Error: q is not a prime") 
        if p <= 100:
            print("Error: p must be larger than 100")
        if q <= 100: 
            print("Error: q must be larger than 100")
        p = input("Enter a large distinct prime p: ")
        p = int(p)
        q = input("Enter a large distinct prime q: ")
        q = int(q)
    n = p*q  
    phiN = phi(p,q)

    print("Your p value is:",p)
    print("Your q value is:",q)    
    print("Your n value is:",n)
    print("Your phi value is:",phiN)

    e = input("Enter a value greater than 1 and less than phi:")
    e = int(e)
    while e >= phiN or e <= 1 or math.gcd(e,phiN) != 1:
        if e >= phiN:
            print("Error: e is too large")
        if e <= 1: 
            print("Error: e is too small")
        if  math.gcd(e,phiN) != 1:
            print("Error: e and phi have a non-one common denominator")
        e = input("Enter a value greater than 1 and less than phi:" )
        e = int(e)
    print("Your e value is:",e)

    return p,q,e

