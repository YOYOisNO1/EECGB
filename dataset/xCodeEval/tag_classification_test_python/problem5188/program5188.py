def program5188():
    
    n, l ,r = map(int, input().split() )
    
    k = n
    a = []
    if n!= 0:
        while k != 0:
            a = [k%2] + a
            k = k//2
    else:
        a = [0]
    count = 0
    for i in range(l, r+1):
        j = 0
        while i %2 ==0:
            i = i//2
            j+=1
        if a[j] == 1:
            count+=1
    print(count)