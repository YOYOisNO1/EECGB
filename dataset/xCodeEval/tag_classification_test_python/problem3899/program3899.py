def program3899():
    a = int(input())
    b = int(input())
    mn = 10**9
    a, b = min(a,b), max(a, b)
    for i in range(a, b+1):
        mn = min(mn, (i - a)*(i-a+1)//2 + (b - i)*(b-i+1)//2)
    print(mn)