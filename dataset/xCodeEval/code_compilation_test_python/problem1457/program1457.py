def two_gram(n,s):
        a = ''
        b = [0:2]
        for i in range(0,len(s)-1):
            if s[i:i+2] in a:
                b = s[i:i+2]
            a += s[i:i+2]
        return b
    
    a = int(input())
    b = str(input())
    print(two_gram(a,b))
    