def main():
        #n, m = map(int, input().split())
    
        _ = int(input())
        a, b, c = map(int, input().split())
        d, e, f = map(int, input().split())
        mini = max(0, a-d-f) + max(0, b-e-d) + max(0, c-e-f)
        maxi = min(a,e)+min(b,f)+min(c,d)
        print(mini, maxi)
    
    
    #input = sys.stdin.readline
    
    #sys.setrecursionlimit(2097152)
    tn = 1 #int(input())
    for _ in range(tn):
        main()