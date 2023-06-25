def program686():
    n, m = map(int, input().split())
    general = list(map(int, input().split()))
    fingers = list(map(int, input().split()))
    
    for item in general:
        for jtem in fingers:
            if item == jtem:
                print(item, end = ' ')