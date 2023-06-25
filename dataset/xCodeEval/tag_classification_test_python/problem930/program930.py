def program930():
    n, a, b = list(map(int, input().split()))
    a, b = min(a, b), max(a, b)
    ans = 1
    while(a!=b-1) or (a%2==0):
        a -= a//2
        b -= b//2
        ans += 1
    lg = 0
    while(n>1):
        lg += 1
        n //= 2
    if(lg == ans):
        print('Final!')
    else:
        print(ans)