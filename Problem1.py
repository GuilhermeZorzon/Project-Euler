def sum_3_5(num):
    i = 0
    soma = 0
    for i in range(num):
        if(i % 3 == 0 or i % 5 == 0):
            soma += i
    return soma; 