def sum_of_3_and_5_multiples(num):
    ''' (int) -> int

    Given an int "num", returns the sum of all multiples of 3 and 5 from 1 to num 

    To use:
    >>> sum_of_3_and_5_multiples(10)
    23 
    '''
    i = 0
    total_sum = 0
    for i in range(num):
        if(i % 3 == 0 or i % 5 == 0):
            total_sum += i
    return total_sum; 