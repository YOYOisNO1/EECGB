    
    #   N
    # W  E
    #  S
    
def go(x,y,cur_fac,t_idx,cells,tlist):
        if t_idx >= len(tlist):
            return None
    
        cells[x][y] = 1
        
        if cur_fac == "N":        
            steps = tlist[t_idx]
            for i in range(steps-1):
                y+=1
                cells[x][y] = 1
            go(x-1,y+1,"NW",t_idx+1,cells,tlist)
            go(x+1,y+1,"NE",t_idx+1,cells,tlist)
    
        if cur_fac == "NW":        
            steps = tlist[t_idx]
            for i in range(steps-1):
                x-=1
                y+=1
                cells[x][y] = 1
            go(x-1,y,"W",t_idx+1,cells,tlist)
            go(x,y+1,"N",t_idx+1,cells,tlist)
    
        if cur_fac == "W":
            steps = tlist[t_idx]
            for i in range(steps-1):
                x-=1
                cells[x][y] = 1
            go(x-1,y+1,"NW",t_idx+1,cells,tlist)
            go(x-1,y-1,"SW",t_idx+1,cells,tlist)
    
        if cur_fac == "SW":
            steps = tlist[t_idx]
            for i in range(steps-1):
                x-=1
                y-=1
                cells[x][y] = 1
            go(x-1,y,"W",t_idx+1,cells,tlist)
            go(x,y-1,"S",t_idx+1,cells,tlist)
    
        if cur_fac == "S":
            steps = tlist[t_idx]
            for i in range(steps-1):
                y-=1
                cells[x][y] = 1
            go(x-1,y-1,"SW",t_idx+1,cells,tlist)
            go(x+1,y-1,"SE",t_idx+1,cells,tlist)
    
        if cur_fac == "SE":
            steps = tlist[t_idx]
            for i in range(steps-1):
                x+=1
                y-=1
                cells[x][y] = 1
            go(x,y-1,"S",t_idx+1,cells,tlist)
            go(x+1,y,"E",t_idx+1,cells,tlist)
    
        if cur_fac == "E":
            steps = tlist[t_idx]
            for i in range(steps-1):
                x+=1
                cells[x][y] = 1
            go(x+1,y+1,"NE",t_idx+1,cells,tlist)
            go(x+1,y-1,"SE",t_idx+1,cells,tlist)
    
        if cur_fac == "NE":
            steps = tlist[t_idx]
            for i in range(steps-1):
                x+=1
                y+=1
                cells[x][y] = 1
            go(x,y+1,"N",t_idx+1,cells,tlist)
            go(x+1,y,"E",t_idx+1,cells,tlist)
    
    d = input()
    tlist = map(int,input().strip().split())
    dim = 2*sum(tlist)+2
    cells = [[0 for i in range(dim)] for i in range(dim)]
    go(dim/2, dim/2, "N", 0, cells, tlist)
    s = 0
    for row in cells[::-1]:
        #print " ".join([str(i) for i in row])
        s += sum(row)
    print s
    
    
        