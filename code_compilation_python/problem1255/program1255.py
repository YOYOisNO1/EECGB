def program1255():
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    out = []
    
    while k>0:
        z = min(arr)
        if z!=101:
            i = arr.index(z)
            if z<=k:
                k -= z
                out.append(i+1)
                arr[i] = 101
        else:
            k=0
    
    print(len(out))
    if len(out)>0:
        print(" ".join([str(i) for i in out]))