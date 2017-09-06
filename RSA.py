
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
  if p!=q:
    if primeCheck(p) and primeCheck(q):
      e = input("Enter number e such that 1<e<(p-1)(q-1)")
      if (1<e and e<phi(p, q)):
        return (e,p,q)
      else:
        print("Error: e is invalid")
        
    
    else:
      print("Error: numbers are not primes")
      
  else:
    print("Error: numbers are identical")
    
    

    
  
    
