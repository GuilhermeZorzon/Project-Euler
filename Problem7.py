def n_prime(n):
    pr_test= 2
    pr_num = 1
    while (pr_num < n):
        pr_test += 1
        isprime = True
        for i in range(2, pr_test):
            if(pr_test % i == 0):
                isprime = False
        if(isprime == True):
            print 
            pr_num += 1
    
    return pr_test
    
        