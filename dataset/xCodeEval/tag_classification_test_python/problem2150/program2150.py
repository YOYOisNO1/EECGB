    import sys
    input = sys.stdin.readline
    
    ############ ---- Input Functions ---- ############
def inp():
        return(int(input()))
def inlt():
        return(list(map(int,input().split())))
def insr():
        s = input()
        return(list(s[:len(s) - 1]))
def invr():
        return(map(int,input().split()))
    
    n=int(input())
    m=n%4
    if m==0:
        print("1 A")
    elif m==1:
        print("0 A")
    elif m==2:
        print("1 B")
    elif m==3:
        print("2 A")