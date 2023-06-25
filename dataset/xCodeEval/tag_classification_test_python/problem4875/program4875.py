def program4875():
    n=input()
    
    x=len(n)
    
    if x==1:
        print(n)
    else:
        max_num="9"*(x-1)
        n=int(n)
        a=n-int(max_num)
    
        a=list(str(a))
        a=[int(item) for item in a]
    
        max_num=list(max_num)
        max_num=[int(item2) for item2 in max_num]
    
        print(sum(a)+sum(max_num))
    
    
    