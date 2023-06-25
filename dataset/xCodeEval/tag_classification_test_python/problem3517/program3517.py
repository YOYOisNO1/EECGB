def program3517():
    a, b, n=map(int, input().split())
    for i in range(102):
        m=0
        if i%2==0:
            for j in range(1, min(a, n)+1):
                if a%j==0 and n%j==0:
                    m=j
        else:
            for j in range(1, min(b, n)+1):
                if b%j==0 and n%j==0:
                    m=j
        n=n-m
        if n==0:
            if i%2==0:
                print(0)
            else:
                print(1)
            break