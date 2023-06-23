def program1899():
    n=int(input())
    a=[]
    i=1
    while(i<=n):
         a.append(i)
         n-=i
         i+=1
    a[-1]+=n
    print(len(a))
    print(*a)//*a give only value