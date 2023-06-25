def program1945():
    n,a,b=map(int,input().split())
    aa=list(map(int,input().split()))
    ba=list(map(int,input().split()))
    out=''
    
    for i in range(1,n+1):
        if i in aa:
            out+='1 '
        elif i in ba:
            out+='2 '
            
    print(out.strip())