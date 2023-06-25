def program1134():
    n,m,k = map(int,input().split())
    
    s = str(((k-1)//2)//m+1)
    s += ' '+str(((k-1)//2)%m+1)
    if(k%2==0):
        s += ' R'
    else:
        s += ' L'
    print(s)