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
        start, start_comp = None, 0
        down = set()
        for i in range(n):
            line = riv()[1:]
            a.append(line)
            if len(line) == 0:
                start = i+1
                start_comp = c[i]
    
        # find next stages
        hours = 1
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
                nz = max(possible.items(), key=lambda z: len(z[1]))
                hours += diff[(start_comp, nz[0])]
                start_comp = nz[0]
                for l in nz[1]:
                    hours += 1
                    down.add(l)
        
        print hours
        
    if __name__ == "__main__":
        main()