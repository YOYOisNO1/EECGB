def program1593():
    import math
    a,b = map(int, input().split())
    n = int(math.sqrt(a))
    if b >= n * (n+1):
        print("Vladik")
    else:
        print("Valera") 