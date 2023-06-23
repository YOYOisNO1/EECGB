def program165():
    # a=list(map(int,input().strip().split()))
    b=int(input())
    g=int(input())
    n=int(input())
    
    # # print(min(n%d,n%(e*5),((n%(e*5))%d),((n%d)%(e*5))))
    # dd=n%d
    # ee=n%(e*5)
    # arr=[dd,ee]
    # if(dd>1):
    #     arr.append((dd+d)%(e*5))
    
    op=[]
    
    j=0
    for k in range(0,n):
        if(((k-j+1)*(j+k))//2>=b and ((k-j+1)*((n-j)+(n-k)))//2>=g):
            op.append(k-j+1)
    print(min(op))