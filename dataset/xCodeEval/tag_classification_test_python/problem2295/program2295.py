def program2295():
    s=input()
    n=str('')
    i=0
    while i <len(s):
        if s[i] == '.':
            n+= str(0)
        if s[i] == '-':
            if s[i+1] == '.':
                n+= str(1)
                i+=1
            else:
                n+= str(2)
                i+=1
        i+=1
    print(n)
    
    # Sat Oct 10 2020 11:26:48 GMT+0300 (Москва, стандартное время)