def program3133():
    n = int(input())
    md = 1000000007
    othernodes = (1<<n)-2
    ans = pow(4,othernodes,md)
    ans = (ans * 6)%md 
    print(ans)