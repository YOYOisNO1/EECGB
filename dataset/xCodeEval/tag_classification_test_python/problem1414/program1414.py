def program1414():
    a, b = map(int, input().split())
    ans = a // b
    a = a % b
    while a > 0:
        ans += b // a
        a, b = b % a, a
    
    print(ans)