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

def encryptor(e,p,q):
    #0 <= C < pq and C === M**e (mod pq).
    
    placeholder = list(input("Enter a word or words you would like encrypted (Unicode 0<=p*q): "))
    i = 0
    j = 0
    interem = 0
    n = p * q
    encryption = []
    placeholdernum = []
    
    while i < len(placeholder): 
        if ord(placeholder[i]) <= 32 or ord(placeholder[i]) >= 122:
          while ord(placeholder[i]) <= 32 or ord(placeholder[i]) >= 122:
            placeholder = list(input("The value(s) are outside of the range, please re-enter: "))
        i = i + 1
    i = 0
    while i < len(placeholder): 
        interem = ord(placeholder[i])
        placeholdernum.append(interem)
        i = i + 1
        
    while j < len(placeholdernum):
        
        if 0 <= placeholdernum[j]: #and placeholdernum[j] <= n:
            encryption.append((placeholdernum[j]**e)%n)
        else:
            print("Please restart the program")
        j = j + 1    
    print("Your encrypted value for ")
    print (placeholder)
    print(" is: ")
    print(encryption)
    return encryption
    #ask for string then deconstruct into encruypted chars and into string array 
    
    
def decryptor(encryptionplaceholder, p , q):
    #R === C**d (mod pq) with 0 <= R < pq.
    n = p * q
    d = input("Enter your secret key d: ")
    d = int(d)
    R = (encryptionplaceholder**d) % n
    if 0 <= R < n:
      print("You decrypted value for ", encryptionplaceholder, " is: ", chr(R))
    else:
       print("Please restart the program")
    #ask for string then deconstruct into encruypted chars and into string array 


def publickeys():
    p = input("Enter a large distinct prime p (100 and greater): ")
    q = input("Enter a large distinct prime q (100 and greater): ")
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
    return e,p,q


def main():
  print("--------~~~-> Public Keys <-~~~--------")
  e, p, q = publickeys()
  print("--------~~~-> Public Keys <-~~~--------")
  print("--------~~~-> Private Key <-~~~--------")
  privateD = privatekey(e, p, q)
  print("--------~~~-> Private Key <-~~~--------")
  print("--------~~~-> Encryptor <-~~~--------")
  encryptedChar = encryptor(e, p, q)
  print("--------~~~-> Encryptor <-~~~--------")
  print("--------~~~-> Decryptor <-~~~--------")
  decryptor(encryptedChar, p, q)
  print("--------~~~-> Decryptor <-~~~--------")

