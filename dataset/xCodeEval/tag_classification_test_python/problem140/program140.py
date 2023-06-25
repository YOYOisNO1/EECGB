def program140():
    n=int(input())
    L=[]
    L=input().split()
    L=[int(i) for i in L]
    b=0
    s=sum(L)
    l=len(L)
    L.sort()
    a=s/l
    while a<4.5:
      b+=1
      L[0]=5
      L.sort()
      a=sum(L)/len(L)
    
    print(b)