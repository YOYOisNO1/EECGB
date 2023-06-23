def program1109():
    from math import log2
    n, a, b = map(int, input().split())
    n1= n
    final = int(log2(n))
    ans = 1
    while(abs(a-b) > 1):
        a//=2
        b//=2
        ans+=1
    if(ans != final):
        print(ans)
    else:
        print("Final!")