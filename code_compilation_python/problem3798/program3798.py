def program3798():
    n,k=map(int,input().split())
    A=input().split()[:n]
    B=[]
    s=0
    ma=int(0)
    for i in range(101):
      B.append([0]*2)
      B[i][0]=i
      B[i][1]=0
    for i in range(n):
      A[i]=int(A[i])
      for j in range(1,101):
        if A[i]==B[j][0]:
          B[j][1]+=1
    for i in range(101):
      if B[i][1]>s:
        s=B[i][1]
      if B[i][1]>0:
    
    if s%k==0:
      ma=s
    elif s<k:
      ma=k
    else:
      ma=int(s/k)*k+k
    s=0
    for i in range(101):
      if B[i][1]>0:
        s+=ma-B[i][1]
    print(s)