def largest_pf(num):
    x = num
    primo = 2
    pr = 1
    while (x > 1):
        if(x % primo == 0):
            x /= primo
        else:
            pr += 1
            primo = prime(pr)
    return primo
            

def prime(num):
    atual = 1
    primo = 2
    j = 1
    while(atual != num):
        teste = primo + j
        i = 2
        falha = False
        while(i < teste):
            if(teste % i == 0):
                falha = True
                j += 1
                break
            i += 1

        if(falha == False):
            atual += 1
            primo += j
            j = 1
        
    return primo     
