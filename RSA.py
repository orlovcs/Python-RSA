
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
  
  
        
def publickeys():
    p = input("Enter a large distinct prime p: ")
    q = input("Enter a large distinct prime q: ")
    p = int(p)
    q = int(q)
    while p==q or not primeCheck(p) or not primeCheck(q):

      if p!=q:
         print("Error: numbers are identical")
      if not primeCheck(p) or not primeCheck(q):
          print("Error: numbers are not primes")
      p = input("Enter a large distinct prime p: ")
      q = input("Enter a large distinct prime q: ")
      p = int(p)
      q = int(q)
    

    
  
    
