def program2142():
    import math
    n = int(input())
    i =int( math.sqrt(n))
    j=i
    while True:
        if i*(i+1)/2+j*(j+1)/2==n:
            print('YES')
            break
        elif i*(i+<n:1)/2+j*(j+1)/2<n:
            j+=1
        else:
            i-=1