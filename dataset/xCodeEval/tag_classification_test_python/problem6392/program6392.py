def program6392():
    if int(input())<3:
     print("no")
     exit(0)
    m=list(map(int,input().split()))
    s=set([(min(m[0],m[1]),max(m[0],m[1]))])
    p=m[1]
    m=m[2:]
    for i in m:
     a,b=min(i,p),max(i,p)
     for c,d in s:
      if a<c<b<d or c<a<d<b:
       print("yes")
       exit(0)
     s.add((a,b))
     p=i
    print("no")