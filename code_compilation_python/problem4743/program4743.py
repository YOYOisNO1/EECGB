def r(): return input().strip()
def ri(): return int(r().strip())
def riv(): return map(int, r().split())
    
    diff = {
        (1,1): 0,
        (2,2): 0,
        (3,3): 0,
        (1,2): 1,
        (1,3): 2,
        (2,1): 2,
        (2,3): 1,
        (3,1): 1,
        (3,2): 2
    }
    
def main():
        n = ri()
        c = riv()
    
        a = []
        starts, start_comps = [], []
        for i in range(n):
            line = riv()[1:]
            a.append(line)
            if len(line) == 0:
                starts.append(i+1) 
                start_comps.append(c[i]) 
    
        min_hours = -1
        while starts:
            hours = 1
            down = set()
            start = starts.pop()
            start_comp = start_comps.pop()
            down.add(start)
            while len(down) < n:
                possible = {}
                for i, stage in enumerate(a):
                    if i+1 not in down and all([s in down for s in stage]):
                        comp = c[i]
                        if comp not in possible:
                            possible[comp] = []
                        possible[comp].append(i+1)
    
                if start_comp in possible:
                    for l in possible[start_comp]:
                        hours += 1
                        down.add(l)
                else:
                    nz = min(possible.items(), key=lambda z: diff[(start_comp, z[0])])
                    hours += diff[(start_comp, nz[0])]
                    start_comp = nz[0]
                    for l in nz[1]:
                        hours += 1
                        down.add(l)
            
            if min_hours == -1 or min_hours > hours:
                min_hours = hours
        
        print min_hours
        
    if __name__ == "__main__":
        main()