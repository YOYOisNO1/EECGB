def program2129():
    from sys import stdin as fin
    # fin = open("cfr417a.in", "r")
    
    # n = int(fin.readline())
    for i in range(4):
        arr = list(map(int, fin.readline().split()))
        if (arr[0] or arr[1] or arr[2]) and arr[3]:
            print("YES")
            break
    else:
        print("NO")