def program4280():
    n = int(input())
    s = input()
    v = ('a','e','i','o','u','y')
    i =0
    while i != n-1:
        if ((s[i] in v) and (s[i+1] in v)):
            s = s[ :i+1] + s[i+2:]
            i =i -1
            n = len(s)
        i =i+1
            
    print(s)