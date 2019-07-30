def sqr_sum_difference(num = 100):
    ''' (int/ ) -> int

    Given num, finds the diference between the sum of all the squares of the numbers lower than num 
    and the square of the sum of these same numbers. Num is set to 100 if no value is passed

    To use:
    >>> sqr_sum_difference(2)
    4
     
    >>> sqr_sum_difference()
    25164150
    '''
    sum_sqr = 0
    sqr_sum = 0
    for i in range(1, num + 1):
        sum_sqr += (i * i)
    for j in range(1, num + 1):
        sqr_sum += j
    sqr_sum *= sqr_sum
    
    return sqr_sum - sum_sqr