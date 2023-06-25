def program2299():
    from itertools import permutations as perm
    
    l = [0, 1, 2, 3, 4] # initial ordering
    
    arr=[]
    
    for i in range(5):  # reading happiness
        arr.append([int(x) for x in input().split()])
    
    ans = -1
    
    for i in perm(l):
        curr = 0
        p = list(i)
        a, b, c, d, e = p[0], p[1], p[2], p[3], p[4]    # diff permutations
        
        curr += (arr[a][b] + arr[b][a] + arr[c][d] + arr[d][c])
        curr += (arr[b][c] + arr[c][b] + arr[d][e] + arr[e][d])
        curr += (arr[c][d] + arr[d][c])
        curr += (arr[d][e] + arr[e][d])
    
        ans = max(ans, curr)    # storing max answer
    
    print(ans)