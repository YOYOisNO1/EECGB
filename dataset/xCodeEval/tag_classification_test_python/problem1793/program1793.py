def program1793():
    x=int(input())
    y=list(map(int,input().split()))
    y.sort()
    print(*y)