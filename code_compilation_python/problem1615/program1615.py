def program1615():
    a,b,c=input().split()
    a1,b1,c1=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    a1=int(a1)
    b1=int(b1)
    c1=int(c1)
    if a+b<=a1+b1 and a<=a1:
        print('YES')
      else:
        print('NO')