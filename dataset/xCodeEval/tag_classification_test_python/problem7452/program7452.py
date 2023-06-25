def program7452():
    li=[1, 3, 15, 133, 2025, 37851, 1030367, 36362925]
    n=int(input())
    fact=[1]
    temp = 1
    for i in xrange(1, 16):
        temp*=i%1000000007
        fact.append(temp)
    if n%2==0:
        print(0)
    else:
        print((li[n/2]) * fact[n])%1000000007