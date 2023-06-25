def program4715():
    n=int(input())
    a=[None]*3
    a[0]=list(map(int,input().split()))
    a[1]=list(map(int,input().split()))
    a[2]=list(map(int,input().split()))
    total=0
    b=[None]*3
    for i in range(3):
          total+=a[i][0]
          b[i]=a[i][0]
    
    while total<n:
          if b[0]<a[0][1]:
                k=a[0][1]-b[0]
                if total+k>n:
                      b[0]+=(n-total)
                      total=n
                else:
                      b[0]+=k
                      total+=k
          if b[1]<a[1][1]:
                k=a[1][1]-b[1]
                if total+k>n:
                      b[1]+=(n-total)
                      total=n
                else:
                      b[1]+=k
                      total+=k
          if b[2]<a[2][1]:
                k=a[2][1]-b[2]
                if total+k>n:
                      b[2]+=(n-total)
                      total=n
                else:
                      b[2]+=k
                      total+=k
          
    print(b[0],b[1],b[2])