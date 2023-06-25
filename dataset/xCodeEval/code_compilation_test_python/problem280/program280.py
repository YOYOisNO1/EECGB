def program280():
    n, k = map(int, input().split())
    a=list(map(int,input().split()))
    if a[k]==a[k]:
        if a[k]>k:
            print(len(a[:k+1]))
        else:
            if a[0]<k:
                print(0)           
            elif a[0]>k:
                print(len(a[0:a[k-1]]))
            else:
                while a==a:
                    k=k+1
                    print(len(a[:k]))
    elif a[k]>k or a[k]==k:
        print(len(a[:k]))
    else:
        print(0)
          
     
        
        