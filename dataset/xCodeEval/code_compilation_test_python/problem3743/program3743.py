def program3743():
    #!/usr/bin/python
    # coding: utf-8
    import sys
    
    lines =[l.strip() for l in sys.stdin.readlines()]
    F = len(lines)
    M_posi = [{'x':0, 'y':F - 1}]
    nexs = []
    ans = 'WIN'
    for l_num in range(F):
        nexs = []
        #Maria move
        for posi in M_posi:
            x = posi['x']
            y = posi['y']
            for i in range(-1, 2):
                nx = x + i
                for n in range(-1, 2):
                    ny = y + n
                    if nx < F and nx > -1 and ny < F and ny > -1:
                        if lines[ny][nx] != 'S':
                            nexs.append({'x':nx, 'y':ny})
        #obstacle move
        lines = lines[:-1]
        lines.insert(0, '........')
        for nex in nexs[:]:
            x = nex['x']
            y = nex['y']
            if lines[y][x] == 'S':
                posi = {'x':x, 'y':y}
                while posi in nexs: nexs.remove(posi)
        if nexs == []:
            ans = 'LOSE'
            break
        M_posi = nexs[:]
    print ans