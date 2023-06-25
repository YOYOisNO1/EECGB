def program509():
    while(1):
        try:
            n=input()
        except EOFError:
            break
        num=[]
        soroban=["O-|-OOOO","O-|O-OOO","O-|OO-OO","O-|OOO-O","O-|OOOO-",
                 "-O|-OOOO","-O|O-OOO","-O|OO-OO","-O|OOO-O""-O|OOOO-"]
        while(n>=0):
            num.append(n%10)
            n=n/10
        for i in num:
            print soroban[i]
        