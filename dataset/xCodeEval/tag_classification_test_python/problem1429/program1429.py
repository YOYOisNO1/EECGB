def readarray(f): return map(f, input().split())
def readint(): return int(input())
def printlist(l): print(' ').join(map(str, l))
    
    n = readint()
    A = readarray(int)
    
    S = sum(A)%(n+1)
    res = 0
    for i in range(1, 6):
      if (S+i)%(n+1) != 1:
        res += 1
    print(res)