def sum_prime():
    # O(n²)
    sumpr = 2
    for i in range(3, 2000000):
        ispr = True
        for j in range(2, i):
            if(i % j == 0):
                ispr = False
        if(ispr == True):
            sumpr += i
            
    return sumpr

def sieve_erastotenes(n):
    # O(n)
    sump = 0
     
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    for p in range(2, n): 
        if prime[p]: 
            sump += p
            
    return sump
