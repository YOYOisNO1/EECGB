def normalize(seg):
        if seg[0] != seg[2] and seg[1] != seg[3]:
            return None
    
        xs = (seg[0], seg[2])
        ys = (seg[1], seg[3])
    
        return (min(xs), min(ys), max(xs), max(ys))
    
def valid(shifted):
        w, h = None, None
        for _, _, x, y in shifted:
            if x != 0 and y != 0:
                if w is not None and (w, h) != (x, y):
                    return False
    
                w, h = x, y
    
        if w is None or h is None:
            return False
    
        expected = [(0, 0, 0, h), (0, 0, w, 0), (0, h, w, h), (w, 0, w, h)]
    
        return set(shifted) == set(expected)
    
def sub(a, x, y):
        return (a[0] - x, a[1] - y, a[2] - x, a[3] - y)
    
def main():
        segs = [normalize(tuple(map(int, input().split()))) for _ in range(4)]
        poss = False
        for seg in segs:
            shifted = [sub(s, seg[0], seg[1]) for s in segs]
            poss |= valid(shifted)
    
        print('YES' if poss else 'NO')
    
    main()