def largest_prime_factor(num):
    ''' (int) -> int

    Given num, returns the largest prime factor of num 

    To use:
    >>> largest_prime_factor(3)
    3

    >>> largest_prime_factor(10)
    5

    >>> largest_prime_factor(49)
    7
    '''
    aux = num
    prime_num = 2

    # Defines the position of the prime to call find_n_prime
    prime_position = 1

    while (aux > 1):
        if(aux % prime_num == 0):
            aux /= prime_num
        else:
            prime_position += 1
            prime_num = find_n_prime(prime_position)
    return prime_num
            

def find_n_prime(n):
    ''' (int) -> int

    Given n, returns the n° prime number 

    To use:
    >>> find_n_prime(1)
    2 
    >>> find_n_prime(2)
    3
    >>> find_n_prime(5)
    11
    '''
    current_prime = 1
    n_prime = 2
    j = 1

    while(current_prime != n):
        test = n_prime + j
        i = 2
        is_prime = True
        while(i < test):
            if(test % i == 0):
                is_prime = False
                j += 1
                break
            i += 1

        if(is_prime == True):
            current_prime += 1
            n_prime += j
            j = 1
        
    return n_prime     
