    r = lambda: input().strip()
    
def check_possibility(new_position, M):
        if len(M) == 0:
            print('WIN')
            exit()
        candidate_moves = []
        for c in [(0,0),(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            new_coord = (new_position[0]+c[0], new_position[1]+c[1])
            if 0 <= new_coord[0] <= 7 and 0 <= new_coord[1] <= 7:
                candidate_moves.append(new_coord)
        candidate_moves = [c for c in candidate_moves if c not in M.keys()]
        M = dict([[(c[0],c[1]+1),'S'] for c in M.keys() if c[1]<7])
        candidate_moves = [c for c in candidate_moves if c not in M.keys()]
        for c in candidate_moves:
            check_possibility(c, dict(M.items()))
    
    
    statue_locations = {}
    for i in xrange(8):
        row = list(r())
        for j in xrange(8):
            if row[j] == 'S':
                statue_locations[(j,i)] = row[j]
    
    
    check_possibility((0,7), dict(statue_locations.items()))
    print('LOSE')