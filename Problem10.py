def find_sum_prime():
    ''' () -> int

    Finds the sum of all the prime numbers below 2.000.000
    '''
    # O(n²)
    sum_prime = 2
    for i in range(3, 2000000):
        is_prime = True
        for j in range(2, i):
            if(i % j == 0):
                is_prime = False
        if(is_prime == True):
            sum_prime += i
            
    return sum_prime

def sieve_of_erastotenes(n):
    ''' (int) -> int

    Finds the sum of all the prime numbers below n using the
    mathematical algorithm "sieve of Erastotenes"
    '''
    # O(n)
    sum_prime = 0
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n + 1, p): 
                prime[i] = False
        p += 1
      
    for p in range(2, n): 
        if prime[p]: 
            sum_prime += p
            
    return sum_prime
