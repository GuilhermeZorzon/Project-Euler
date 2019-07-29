def hg_palindrome():
    
    for i in range(100, 1000):
        for j in range(100, 1000):
            mult = i * j
            smult = str(mult)
            pal = True
            for c in range(len(smult)):
                if(smult[c] != smult[len(smult)- 1 - c]):
                    pal = False
            if(pal == True):
                print("Palindromo: ", mult)
    
