def fibonacci_even_terms_sum(num):
    ''' (int) -> int
    
    Given an int "num", returns the sum of all Fibonacci even-valued terms whose values do not exceed num

    To use:
    >>> fibonacci_even_terms_sum(10)
    10 
    '''
    # Son and father are the terminology used to refer to, respectively, the previous and the next number in the Fibonacci sequence
    son = 1
    father = 1
    # Used nxt since next is a keyword
    nxt = 1
    total = 0
    while(son + father <= num):
        nxt = son + father
        son = father
        father = nxt
        if(nxt % 2 == 0):
            total += nxt
    return total