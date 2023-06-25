def f(t):
        tp = 1+(4*t)
        return int(abs(min((((-1)+(tp**0.5))/2),(((-1)-(tp**0.5))/2))))   
    
    d = int(input())
    s = input()
    n = f(2*d)-1
    ans = ''
    for i in range(n,0,-1):
        d-=i
        l1 = s[d:]
        ans += l1[0]
        s = s[0:d]
    print(ans[::-1])