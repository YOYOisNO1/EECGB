def program3557():
    n,t = [int(x) for x in input().split()]
    L= input()
    for i in range(t):
        L = L.replace('BG','GB')
    print(L)