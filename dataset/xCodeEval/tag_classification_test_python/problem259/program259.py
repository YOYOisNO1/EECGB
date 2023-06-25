def program259():
    from sys import stdin, stdout
    
    
    n, c = map(int, stdin.readline().split())
    ar = list(map(int, stdin.readline().split()))
    
    ans = 0
    
    for i in range(n - 1):
        if ar[i] - ar[i + 1] - c >= ans:
            ans = ar[i] - ar[i + 1] - c
    
    stdout.write(str(ans) + '\n')