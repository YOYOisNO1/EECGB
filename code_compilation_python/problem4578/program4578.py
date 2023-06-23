    class card:
    def __init__(self, one, two):
            self.c = one
            self.t = two
    
    
    inp = []
    chars = {'R': 0, 'G': 1, 'B': 2, 'Y': 3, 'W': 4}
    n = int(input())
    spl = input().split(' ')
    for s in spl:
        inp.append(card(chars[s[0]], int(s[1]) - 1))
    
    
def check(mask):
        for i in xrange(n):
            for j in xrange(i + 1, n):
                c1 = inp[i]
                c2 = inp[j]
                flag = False
                if c1.c == c2.c and c1.t == c2.t:
                    flag = True
                if c1.c != c2.c and ((mask & (1 << c1.c)) != 0 or (mask & (1 << c2.c)) != 0):
                    flag = True
                if c1.t != c2.t and ((mask & (1 << (c1.t + 5))) != 0 or (mask & (1 << (c2.t + 5))) != 0):
                    flag = True
                if not flag:
                    return False
        return True
    
    
def count_bits(mask):
        out = 0
        while mask > 0:
            if mask & 1 == 1:
                out += 1
            mask >>= 1
        return out
    
    out = 10
    end = 2 ** 10
    for m in xrange(end):
        if check(m):
            #print m, bin(m), count_bits(m)
            out = min(out, count_bits(m))
    
    print out