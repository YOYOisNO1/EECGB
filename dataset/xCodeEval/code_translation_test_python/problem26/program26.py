    # enumerate range float sorted reversed
def print_ints(a):
        print(' ').join(map(str, a))
    
def f(l):
        s = 0
        i = 0
        n = len(l)
        need = n*4.5
        s = sum(l)
        c = 0
        for e in sorted(l):
            if s >= need:
                break
            s += (5-e)
            c += 1
        print(c)
        return
            
    
    read_ints = lambda: map(int, input().strip().split())
    read_floats= lambda: map(float, input().strip().split())
    n = int(input())
    l = read_ints()
    
    f(l)