def program1666():
    import math
    f = {}
    s = input()
    for c in s:
        if c in f:
            f[c]+=1
        else:
            f[c]=1
    [nb,ns,nc] = [int(i) for i in input().split() ]
    [pb,ps,pc] = [int(i) for i in input().split() ]
    
    h = int(input())
    x=0
    mn = 0 
    mx = 1000000000000
    
    while(mn<=mx):
        x = math.ceil((mn+mx)/2);
        fx =  (f['B']*x-nb)*pb+(f['C']*x-nc)*pc+(f['S']*x-ns)*ps
        if fx<=h:
            mn = x+1
        else:
            mx = x-1
    
    print(x)