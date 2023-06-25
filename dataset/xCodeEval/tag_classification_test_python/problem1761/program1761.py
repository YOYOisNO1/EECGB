def program1761():
    n = int(input())
    arr = [int(i) for i in input().split()]
    sums = [0]
    add = 0
    for a in arr:
        add += 1 if a==1 else 0
        sums.append(add)
    if n==1:
        if arr[0]==0:
            mx = 1
        else:
            mx = 0
    else:
        mx = sums[-1]-1
        for i in range(1, n):
            for j in range(i+1, n+1):
                l = j-i+1
                ones = sums[j]-sums[i-1]
                zeroes = l-ones
                mx = max(mx, sums[-1]+zeroes-ones)
    print(mx)