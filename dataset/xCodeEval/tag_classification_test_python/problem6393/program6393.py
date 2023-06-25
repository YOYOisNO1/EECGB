def program6393():
    input()
    v = list(map(int, input().split()))
    
    w = [(min(v[x], v[x+1]), max(v[x], v[x+1])) for x in range(0, len(v)-1)]
    
    for i in range(0, len(w)):
        for j in range(0, len(w)):
            if i == j: continue
            
            a, b = w[i][0], w[i][1]
            c, d = w[j][0], w[j][1]
    
            if a < c and c < b and (d < a or d > b):
                print('yes')
                exit()         
    print('no')
     