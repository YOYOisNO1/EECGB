def program4231():
    p=0
    n=int(input())
    if n==1:
        print('-1')
    else:
        for i in range(2,n+1):
            for k in range(1,n+1):
                if i*k>n and i%k==0 and i*k>n and i/k<n:
                    print(i,k)
                    p=1
                    break
            if p==1:
                break