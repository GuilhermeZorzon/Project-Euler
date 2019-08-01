from math import sqrt

def find_special_pitagorical_triplet():
    ''' () -> int

    Finds the special pitagorical triplet whose sum a + b + c = 1000 
    and returns the product a * b * c
    '''
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = sqrt((a * a) + (b * b))
            if(a + b + c == 1000):
                print("a, b, c: ", a, b, c)
                return a * b * c
                
    print("a, b, c: ", a, b, c)
    return a * b * c