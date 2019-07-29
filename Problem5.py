def evl_div():
    num = 2520
    achou =  False 
    while(achou == False):
        evl = True
        for i in range(20):
            if(num % (i+1) != 0):
                evl = False
                break
        if(evl == True):
            achou = True
        else:
            num += 1
            
    return num
        
def evl_div_ch(num):
    n = num 
    achou =  False 
    while(achou == False):
        evl = True
        for i in range(num):
            if(n % (i+1) != 0):
                evl = False
                break
        if(evl == True):
            achou = True
        else:
            n += 1
            
    return n