''' This function could be enhanced in terms of code complexity if it started "mult" with 1000 * 1000, not 100 * 100.
    It would not change the O(n²) of the algorithm, since it would still be O(n²) in the worst case. However,
    in real life terms, it would considerably enhance the time it takes to find an answer
'''

def find_largest_3digit_palindrome_product():
    
    palindrome = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            # Set the product
            product = i * j
            str_product = str(product)
            is_palindrome = True
            for c in range(len(str_product)):
                if(str_product[c] != str_product[len(str_product)- 1 - c]):
                    is_palindrome = False
            if(is_palindrome == True):
                palindrome = product
    print("The largest palindrome made from the product of two 3-digit numbers is " + str(palindrome) + ", result of the product of " + str(i) + " and " + str(j) )
    
