def program3162():
    #m = int(input())
    #n = int(input())
    n,m = map(int,input().split())
    #print(m,n)
    a = int((n/2))+1
    if m>n:
      a=n
    elif m>=a:
      a = m-1
    else:
      a = m+1
    if a>n or a<1:
      a=n
    print(a)