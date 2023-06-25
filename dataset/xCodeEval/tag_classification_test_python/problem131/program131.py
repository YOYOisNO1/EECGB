def program131():
    
    
    n = int(input())
    
    
    i=1
    while n>=i:
        n-=i
        i+=1
    print(str(i-1))
    
    re=''
    for x in range(i-2):
        re=re+str(x+1)+' '
    re=re+str(i-1+n)
    print(re)
    