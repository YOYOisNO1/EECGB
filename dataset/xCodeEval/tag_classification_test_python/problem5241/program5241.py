def program5241():
    import sys
    
    n , m = map(int,sys.stdin.readline().split())
    mod_res = [0]*5
    for i in range(1,m+1) :
        mod_res[i%5] += 1
    
    ans = 0
    for i in range(1,n+1) :
        ans += mod_res[(5-(i%5))%5]
    
    print(ans)