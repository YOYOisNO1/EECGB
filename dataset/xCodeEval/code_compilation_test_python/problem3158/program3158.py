def program3158():
    n,m=map(int,input().split())
    narr=[(n//5),(n//5)+min(1,n%5),(n//5)+(min(2,n%5))//2,
          (n//5)+(min(3,n%5))//3,(n//5)+(min(4,n%5))//4 ]
    marr=[(m//5),(m//5)+min(1,m%5),(m//5)+(min(2,m%5)//2,
          (m//5)+(min(3,m%5))//3,(m//5)+(min(4,m%5))//4 ]
    count=0
    for i in range(5):
        count+=narr[i]*marr[-i]
    print(count)