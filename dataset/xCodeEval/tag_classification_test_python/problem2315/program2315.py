    import sys
    input = sys.stdin.readline
    import time
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
    
    n = inp()
    
    start = time.process_time()
    
    
    
    bills = [100, 20, 10, 5, 1]
    
    nb_bills = 0
    
    for bill in bills:
        count = n//bill
        n -= count*bill
        nb_bills += count
    
    print(nb_bills)
    # print(time.process_time() - start) 