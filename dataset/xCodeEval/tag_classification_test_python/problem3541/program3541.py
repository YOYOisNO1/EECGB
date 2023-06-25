def program3541():
    n, t = map(int, input().split())
    a = input()
    i,j = 0, 0
    while j < t:
        i = 0
        while i < n:
            if a[i] == 'B' and i != n -1:
                if a[i+1] == 'G':
                    a = a[:i]+'GB'+a[i+2:]
                    i+=2
                else:
                    i+=1
            else:
                i+=1
        j+=1
    print(a)