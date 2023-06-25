def program6056():
    r = input()
    k = input()
    
    ab = 'abcdefgh'
    
    r_d = [ab.index(r[0])+1, int(r[1])]
    k_d = [ab.index(k[0])+1, int(k[1])]
    
    board = [[0 for i in range(8)] for j in range(8)]
    
    bad1 = [r[0]+str(j) for j in range(1,9)] # rook can take knight 2
    bad2 = [i+r[1] for i in 'abcdefgh'] # rook can take knight 2
    bad3 = []
    
    for i in range(1,9):
        for j in range(1,9):
            if (((i-r_d[0])**2 + (j-r_d[1])**2) == 5) or (((i-k_d[0])**2 + (j-k_d[1])**2) == 5):
                bad3.append(ab[i-1]+str(j))
    
    bad = set(bad1+bad2+bad3+[k])
    
    print(64 - len(bad))
    