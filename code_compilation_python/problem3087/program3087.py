    import sys
    read=lambda:sys.stdin.readline().rstrip()
    readi=lambda:int(sys.stdin.readline())
    writeln=lambda x:sys.stdout.write(str(x)+"\n")
    write=lambda x:sys.stdout.write(x)
def solve(memory, N):
        if N == 1:
            return "YES"
        pad=[[-1]*7 for _ in range(8)]
        n = 1
        npos = [[-1,-1]]*10
        for i in range(2, 5):
            for j in range(2, 5):
                pad[i][j] = n
                npos[n] = (i, j)
                n += 1
        pad[5][3] = 0
        npos[0] = (5, 3)
        vecs = []
        sy, sx = npos[int(memory[0])]
        for i in range(N-1):
            y, x = npos[int(memory[i])]
            ny, nx = npos[int(memory[i+1])]
            vecs.append((ny-y, nx-x))
    
        for i in range(2, 5):
            for j in range(2, 5):
                if (sy, sx) == (i, j):
                    continue 
                y, x = i, j
                for t in range(N-1):
                    dy,dx = vecs[t]
                    y, x = y + dy, x + dx
                    if pad[y][x] == -1:
                        break
                else:
                    return "NO"
        
        if (sy, sx) == (5, 3):
            return "YES"
        
        y, x = 5, 3
        for t in range(N-1):
            dy,dx = vecs[t]
            y, x = y + dy, x + dx
            if pad[y][x] == -1:
                break
        else:
            return "NO"
    
        return "YES"
    
    N=readi()
    mem = read()
    writeln(solve(mem, N))