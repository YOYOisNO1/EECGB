    """
        Author : thekushalghosh
        Team   : CodeDiggers
    """
    import sys,math
    input = sys.stdin.readline
    ############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
        return(int(input()))
def inlt():
        return(list(map(int,input().split())))
def insr():
        s = input()
        return(s[:len(s) - 1])
def invr():
        return(map(int,input().split()))
    ################################################################
    ############ ---- THE ACTUAL CODE STARTS BELOW ---- ############
    t = 1
    for tt in range(t):
        u, v = map(int, input().split())
        if u == 0 and v == 0:
            print(0)
        elif u == 0 or v == 0:
            print(-1)
        q = list(map(int,list(reversed(list("0" * (60 - int((math.log(u) // math.log(2)) + 1)) + bin(u).replace("0b", ""))))))
        w = list(map(int,list(reversed(list("0" * (60 - int((math.log(v) // math.log(2)) + 1)) + bin(v).replace("0b", ""))))))
        qw = 0
        for i in range(59,-1,-1):
            if w[i] % 2 == q[i]:
                continue
            if i == 0:
                qw = 1
                break
            if q[i] == 1 and w[i] == 0:
                for j in range(i + 1, 60):
                    if w[j] >= 2:
                        w[j] = w[j] - 2
                        for k in reversed(range(i, j)):
                            w[k] = w[k] + 2
                        w[i] = w[i] + 4
                        break
                if w[i] == 0:
                    qw = 1
                    break
            w[i] = w[i] -  1
            w[i - 1] = w[i - 1] + 2
        if qw == 1:
            print(-1)
        else:
            qwqw = [0] * max(w)
            for i in range(60):
                for j in range(w[i]):
                    qwqw[j] = qwqw[j] + 2 ** i
            print(len(qwqw))
            print(*qwqw)