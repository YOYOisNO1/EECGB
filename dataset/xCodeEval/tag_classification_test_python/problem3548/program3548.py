def program3548():
    n, t = map(int, input().split())
    arr = list(input())
    for i in range(t):
        swp = False
        for j in range(n-1):
            if swp:
                swp = False
                continue
            elif arr[j]=='B' and arr[j+1]=='G':
                arr[j] = 'G'
                arr[j+1] = 'B'
                swp = True
    print("".join(arr))