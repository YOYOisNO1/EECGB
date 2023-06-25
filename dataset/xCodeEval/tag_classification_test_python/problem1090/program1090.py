def program1090():
    n = int(input())
    for _ in range(1):
        a1,a2,a3 = map(int,input().split())
        b1,b2,b3 = map(int,input().split())
        ansa = min(a1,b2)+min(a2,b3)+min(a3,b1)
        ansb = min(a1, n - b2) + min(a2, n - b3) + min(a3, n - b1)
        print(n - ansb)
        print(ansa)