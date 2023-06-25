def program962():
    n = int(input()) #num of rounds
    
    a = input().split() #alice's strategy
    a = [int(play) for play in a]
    
    b = input().split() #bob's strategy
    b = [int(play) for play in b]
    
    #max of alice's victorys
    amax = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    
    #mix of alice's victorys
    amin = n - (min(a[0], b[2] + b[0]) + min(a[1], b[0] + b[1]) + min(a[2], b[1] + b[2]))
    
    print(amin, amax)