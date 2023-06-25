def program3450():
    import sys,math
    from collections import defaultdict
    from io import BytesIO
    
    sys.stdin = BytesIO(sys.stdin.read())
    input = lambda: sys.stdin.readline().rstrip('\r\n')
    #n = int(input())
    #n,k = [int(x) for x in input().split(' ')]
    #arr = [int(x) for x in input().split(' ')]
    arr = []
    for i in range(4):
        arr.append(int(input()))
    if arr[2] > 0:
        print(1 if arr[0] == arr[3] and arr[0] > 0 else 0)
    else:
        print(1 if arr[0] == arr[3] else 0)