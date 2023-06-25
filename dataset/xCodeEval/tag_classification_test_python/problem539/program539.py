def remove_zeroes( n ):
        s = str(n)
        l = ''
        for i in s:
            if (i!= '0'):
                l+= i
        return int(l)
    n = int (input())
    m = int (input())
    res = n + m
    if remove_zeroes(n)+ remove_zeroes(m) == remove_zeroes(res):
        print("YES")
    else :
        print("NO")