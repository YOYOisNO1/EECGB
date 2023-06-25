def program4075():
    __author__ = 'asmn'
    a,c=tuple(map(int,input().split()))
    b,mul=0,1
    while not (a==0 and c==0):
        b+=(c%3-a%3+3)%3*mul
        a//=3
        c//=3
        mul*=3
    print(b)