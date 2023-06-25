def program3549():
    n,m = map(int,input().split())
    s = input()
    l = list(s)
    c = False
    for j in range(m):
       c = False
       for i in range(n-1):
          #print(i,l[i])
          if c: c = False;continue
          if l[i]=="B" and l[i+1]=="G":
             l[i],l[i+1] = l[i+1],l[i]
             c = True
             #print(l)
    
    k = ''
    for i in l:
       k+=i
    print(k,)