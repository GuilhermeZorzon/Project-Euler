def sqr_sum_dif():
    num = 100
    sum_sqr = 0
    sqr_sum = 0
    for i in range(1, num + 1):
        sum_sqr += (i * i)
    for j in range(1, num + 1):
        sqr_sum += j
    sqr_sum *= sqr_sum
    
    return sqr_sum - sum_sqr