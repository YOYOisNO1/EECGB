def program1402():
    n,m,a,b = map(int,input().split())
    a=a-1
    if (a%m==0 and (b%m ==0 or b==n)) or (a/m==b/m): print(1)
    elif a%m == b%m or a%m==0 or b%m==0 or b==n or (abs(a/m-b/m)==1): print(2)
    else: print(3)