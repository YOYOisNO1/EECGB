def program3647():
    n,t = [int(x) for x in input().split()]
    l = input()
    #length = len(l)
    for i in range(t):
        #l2 = l.copy()
        ind = 0
        while True:
            try:
                ind = l[ind:].index('BG') + ind
                l = l[:ind] + 'GB' + l[ind+2:]
                ind += 2
            except:
                break
    print(l)