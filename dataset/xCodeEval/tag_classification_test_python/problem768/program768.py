def program768():
    t = int(input())
    
    for tt in range(t):
        m = int(input())
    
        keys = [0] + list(map(int, input().split(" ")))
    
        ans = keys[m] * keys[keys[m]]
    
        print( "YES" ) if ans else print("NO")