def program1321():
    import math
    inp = input()
    inp = inp.split(' ')
    n = int(inp[0])
    k = int(inp[1])
    st=10**k
    NOD = math.gcd(n,st)
    NOK = n*st/NOD
    print(int(NOK))