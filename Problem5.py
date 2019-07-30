def find_smallest_number_evenly_divised_1to20():
    ''' ( ) -> int

    Finds the smallest number who can be evenly divised by all the natural numbers from 1 to 20
    '''
    num = 2520
    has_found =  False 
    while(has_found == False):
        is_even = True
        for n in range(20):
            if(num % (n + 1) != 0):
                is_even = False
                break
        if(is_even == True):
            has_found = True
        else:
            num += 1
            
    return num
        
def found_smallest_number_evenly_divised(num):
    ''' (int) -> int

    Finds the smallest number who can be evenly divised by all the natural numbers from 1 to num

    To use:
    >>> found_smallest_number_evenly_divised(3)
    6 
    '''
    n = num 
    has_found =  False 
    while(has_found == False):
        is_even = True
        for i in range(num):
            if(n % (i + 1) != 0):
                is_even = False
                break
        if(is_even == True):
            has_found = True
        else:
            n += 1
            
    return n