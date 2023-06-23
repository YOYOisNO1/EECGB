    board=[]
    for row in range(9)
    	board.append(list(input()))
    
def check(infile):
        count = 0
        for i in range (0,9):
            for j in range(0,9):
                if infile[i].count(infile[i][j]) <= 1:
                    count = count + 0
                else:
                    count = count + 1
    
    cols = [[row[i] for row in infile] for i in[0,1,2,3,4,5,6,7,8]]
    leg = 0
    for i in range(0,9):
        for j in range(0,9):
            if cols[i].count(cols[i][j]) <= 1:
                leg = leg + 0
            else:
                    leg = leg + 1
    
    angel = []
    for t in range(3):
        ang = infile[t]
        for u in range(3):
            angel.append(ang[u])
    
            foot = 0
            for be in range(9):
                if angel.count(angel[be]) <= 1:
                    foot = foot + 0
                else:
                        foot = foot + 1
    
    
    if count + leg + foot == 0:
        print("Valid")
    else: