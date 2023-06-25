def program1034():
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())
    print(max(b1-a1-a2, b2-a3-a2, b3-a1-a3, 0), min(a3, b1) + min(a2, b3) + min(a1, b2))