def program1452():
    n = input()
    a = map(int, input().split())
    
    print(2 + (min(a) ^ a[2]))