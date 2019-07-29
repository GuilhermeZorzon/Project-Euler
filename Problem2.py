def fibonacci_sum(num):
    son = 1
    father = 1
    nxt = 1
    soma = 0
    while(son + father <= num):
        nxt = son + father
        son = father
        father = nxt
        if(nxt % 2 == 0):
            soma += nxt
    return soma