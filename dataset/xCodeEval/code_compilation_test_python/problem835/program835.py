    #!/usr/bin/env python3
def solve(a,b):
        if a == 1 and b == 1:
            return 1
        else:
            a, b = max(a, b), min(a, b)
            return 1 + solve(a - b, b)
    a, b = map(int,input().split())
    print(solve(a,b))