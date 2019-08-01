def find_n_prime(n):
    ''' (int) -> int

    Given n, returns the n° prime number

    To use:
    >>> find_n_prime(1)
    2

    >>> find_n_prime(4)
    7
    '''

    prime_test= 2
    prime_num = 1
    while (prime_num < n):
        prime_test += 1
        is_prime = True
        for i in range(2, prime_test):
            if(prime_test % i == 0):
                is_prime = False
        if(is_prime == True): 
            prime_num += 1
    
    return prime_test
    
        