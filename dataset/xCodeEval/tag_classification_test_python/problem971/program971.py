def program971():
    from itertools import permutations
    
    n = int(input())
    RA,SA,PA = map(int,input().split())
    RB,SB,PB = map(int,input().split())
    
    alice = {"RA":RA,"SA":SA,"PA":PA}
    bob = {"RB":RB,"SB":SB,"PB":PB}
    
    minimum = maximum = 0
    
    # first three moves to lose then make draws if something remains that is the value
    moves = [["RA","PB"],["SA","RB"],["PA","SB"],["RA","RB"],["SA","SB"],["PA","PB"]]
    perm = list(permutations(moves))
    
    minimum = float('inf')
    for move in perm:
        acopy , bcopy = alice.copy(),bob.copy()
        for a,b in move:
            val = min(acopy[a],bcopy[b])
            acopy[a]-=val
            bcopy[b]-=val
    
        temp = min(acopy["RA"],bcopy["SB"]) + min(acopy["SA"],bcopy["PB"]) + min(acopy["PA"],bcopy["RB"])
        minimum = min(minimum,temp)
    
    maximum = min(alice["RA"],bob["SB"]) + min(alice["SA"],bob["PB"]) + min(alice["PA"],bob["RB"])
    print(f'{minimum} {maximum}')