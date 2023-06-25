def program985():
    import math
    n, m, t=map(int,input().split())
    ans=math.factorial(n+m)
    ans=ans/math.factorial(n+m-t)
    ans=ans/math.factorial(t)
    if n>=t:
        ans1=math.factorial(n)
        ans1=ans1/math.factorial(t)
        ans1=ans1/math.factorial(n-t)
        ans=ans-ans1
    if m>=t:
        ans1=math.factorial(m)
        ans1=ans1/math.factorial(t)
        ans1=ans1/math.factorial(m-t)
        ans=ans-ans1
    if m+1>=t:
        k=math.factorial(n)/math.factorial(1)/math.factorial(n-1)
        ans1=math.factorial(m)
        ans1=ans1/math.factorial(t-1)
        ans1=ans1/math.factorial(m+1-t)
        ans1=ans1*k
        ans=ans-ans1
    if m+2>=t:
        k=math.factorial(n)/math.factorial(2)/math.factorial(n-2)
        ans1=math.factorial(m)
        ans1=ans1/math.factorial(t-2)
        ans1=ans1/math.factorial(m+2-t)
        ans1=ans1*k
        ans=ans-ans1
    if m+3>=t:
        k=math.factorial(n)/math.factorial(3)/math.factorial(n-3)
        ans1=math.factorial(m)
        ans1=ans1/math.factorial(t-3)
        ans1=ans1/math.factorial(m+3-t)
        ans1=ans1*k
        ans=ans-ans1
    print(ans)