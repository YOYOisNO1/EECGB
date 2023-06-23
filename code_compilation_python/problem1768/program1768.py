def program1768():
    n,k,x=map(int,input().split())
    a=list(map(int,input().split()))
    if(len(a))<=2:
        print(k*x)
    else:
         a.remove(max(a))
          a.remove(max(a))
         print(sum(a)+k*x)