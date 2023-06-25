    #!/usr/bin/python3
    
    import sys
    
    n = int(sys.stdin.readline())
    cards = list(set(sys.stdin.readline().split()))
    
    m = 10  # Minimal number of hints
    
def count_ones(n):
        cnt = 0
        while n > 0:
            if n & 1:
                cnt += 1
            n //= 2
        return cnt
    
def split(l, c):
        a, b = [], []
        for card in l:
            if c in card:
                a.append(card)
            else:
                b.append(card)
        return a, b
    
def is_clear(cards, h):
        cl = [cards]
        namig = 'RGBYW12345'
        for i in range(10):
            hint = (h & 1) == 1
            h //= 2
            if not hint: continue
            
            cl2 = []
            for c in cl:
                a, b = split(c, namig[i])
                if len(a) >= 2:
                    cl2.append(a)
                if len(b) >= 2:
                    cl2.append(b)
            cl = cl2
            # print(cl)
        cl = [x for x in cl if len(x) >= 2]
        return len(cl) == 0
    
    for h in range(2**10):
        hints = count_ones(h)
        if is_clear(cards, h):
            m = min(m, hints)
    
    print(m)