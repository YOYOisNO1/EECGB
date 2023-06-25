def program3600():
    import sys
    inputs1 = sys.stdin.readline().split()
    n = int(inputs1[0])
    t = int(inputs1[1])
    sQueue = sys.stdin.readline().strip()
    for sec in range(t):
        flag = False
        for i in range(n):
            if flag: 
                flag = False
                continue
            if sQueue[i] == "B" and i != n -1 and sQueue[i+1] == "G":
                sQueue = sQueue[:i] + sQueue[i+1] + sQueue[i] + sQueue[i+2:]
                flag = True
    print(sQueue)