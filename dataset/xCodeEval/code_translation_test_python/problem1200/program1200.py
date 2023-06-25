def program1200():
    S = input()
    n1, n2, n3 = map(int, input().split())
    p1, p2, p3 = map(int, input().split())
    r = int(input())
    m1, m2, m3 = S.count('B'), S.count('S'), S.count('C')
    L = 0;
    R = 10000000000000
    while L < R:
        mid = (L + R + 1) // 2
        fee = max(0, mid * m1 - n1) * p1 + max(0, mid * m2 - n2) * p2 + max(0, mid * m3 - n3) * p3
        if r >= fee:
            L = mid
        else:
            R = mid - 1
    
    print(int(L))