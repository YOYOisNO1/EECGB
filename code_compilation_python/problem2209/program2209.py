def read():
        return [int(x) for x in input().split(" ")]
    
    n, m = read()
    I = read()
    a = [0] * (n+1)
    for i in range(m-1):
        current = I[i]
        next = I[i+1]
        val = (next - current) % n
        if val in a and a[I[i]] != val:
            print("-1")
            break
        elif a[I[i]] != 0 and a[I[i]] != val:
        a[I[i]] = val if val != 0 else n
    
    else:
        j = []
        for num in range(1, n+1):
            if num not in a:
                j.append(num)
        k = 0
        for i, num in enumerate(a[1:]):
            if num == 0:
                a[i+1] = j[k]
                k += 1
        print(' '.join(map(str,a[1:])))