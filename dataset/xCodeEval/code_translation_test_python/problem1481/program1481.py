def program1481():
    a = list(input())
    n = ['B', 'A', 'C']
    for k in range(len(a)):
        if a[k] in n and k < len(a)-1 and k > 0:
            if a[k-1] in n and a[k+1] in n:
                if a[k-1] != a[k+1] and a[k-1] != a[k] and a[k] != a[k+1]:
                    print('Yes')
                    break
    else:
        print('No')