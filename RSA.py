
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


    
  
    