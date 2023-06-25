def prime(x) :
        if x == 2 : return 1
        if ~ x & 1 : return 0
        i = 3
        while i * i <= x :
            if x % i == 0 : return 0
            i += 1
        return 1
    n = int(input())
    cnt = 0
    for i in range (2, int(1e9), 1) :
        if not prime(i) : continue
        if i == int(str)(i)[::-1]) : continue
        if not prime(int(str(i)[::-1])) : continue
        cnt += 1
        if cnt == n : exit(print(i))