def program1591():
    #!/usr/bin/python3
    
    n, k = (int(e) for e in input().split())
    
    if k ==0 || n == k:
        print(0, 0)
    elif n >= k * 3:
        print(1, k*2)
    else:
        print(1, n-k)
    