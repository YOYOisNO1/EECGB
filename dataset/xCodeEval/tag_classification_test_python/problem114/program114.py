    import sys
    sys_in = sys.stdin
    
    
def read_ints():
        return map(lambda x: int(x), sys_in.readline().split())
    
    
def read_int():
        return int(sys_in.readline())
    
    N = read_int()
    line = sys_in.readline().strip()
    
    possible_colors = [None]*N
    for i in range(N):
        c = line[i]
        if c != '?':
            possible_colors[i] = set([c])
            if i > 0:
                try:
                    possible_colors[i-1].remove(c)
                except KeyError:
                    pass
        else:
            possible_colors[i] = set(['C', 'M', 'Y'])
            if i > 0:
                if len(possible_colors[i-1]) == 1:
                    possible_colors[i].remove(list(possible_colors[i-1])[0])
        if len(possible_colors[i]) == 0:
            sys.stdout.write("No\n")
            exit(0)
    
    for i in range(N-1, 0, -1):
        if len(possible_colors[i]) == 0:
            sys.stdout.write("No\n")
            exit(0)
        if len(possible_colors[i]) == 1:
            try:
                possible_colors[i-1].remove(list(possible_colors[i])[0])
            except KeyError:
                pass
    
    for i in range(N):
        if len(possible_colors[i]) == 0:
            break
        if len(possible_colors[i]) >= 2:
            sys.stdout.write("Yes\n")
            exit(0)
    
    sys.stdout.write("No\n")