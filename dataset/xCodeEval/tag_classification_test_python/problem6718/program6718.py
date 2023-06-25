    class Segment:
    def __init__(self, start, values):
            self.start = start
            self.values = values
    
    def __repr__(self):
            return repr((self.start, self.values))
    
    def get(self, i):
            if i < self.start or self.start + len(self.values) <= i:
                return None
            return self.values[i - self.start]
    
    
def one(n):
        return (10 ** n - 1) // 9
    
    
    INF = 10 ** 100
    
    
def merge(segs):
        result = []
        s = -1
        new_seg = Segment(-1, [])
        while True:
            minv = INF
            for seg in segs:
                v = seg.get(s)
                if v is not None:
                    minv = min(minv, v)
            if minv == INF:
                if new_seg.values:
                    result.append(new_seg)
                ns = INF
                for seg in segs:
                    if s < seg.start:
                        ns = min(ns, seg.start)
                if ns == INF:
                    break
                s = ns
                new_seg = Segment(s, [])
            else:
                new_seg.values.append(minv)
                s += 1
        return result
    
    
def solve(n):
        pos = [Segment(n, [0])]
        neg = []
        for length in range(len(str(n)) + 1, 0, -1):
            pre_one = one(length + 1)
            cur_one = one(length)
            new_pos = []
            new_neg = []
            for seg in pos:
                s = seg.start
                k = s // cur_one
                r = s % cur_one
                new_pos_seg = Segment(r, [])
                new_neg_seg = Segment(r, [])
                for v in seg.values:
                    new_pos_seg.values.append(v + k * length)
                    new_neg_seg.values.append(v + (k + 1) * length)
                    if r + 1 == cur_one:
                        new_pos.append(new_pos_seg)
                        new_neg.append(new_neg_seg)
                        k += 1
                        r = 0
                        new_pos_seg = Segment(0, [])
                        new_neg_seg = Segment(0, [])
                    else:
                        r += 1
                if new_pos_seg.values:
                    new_pos.append(new_pos_seg)
                    new_neg.append(new_neg_seg)
            for seg in neg:
                s = pre_one - seg.start
                k = (pre_one - seg.start - 1) // cur_one
                r = (seg.start - pre_one) % cur_one
                new_pos_seg = Segment(r, [])
                new_neg_seg = Segment(r, [])
                for v in seg.values:
                    new_neg_seg.values.append(v + k * length)
                    new_pos_seg.values.append(v + (k + 1) * length)
                    if r + 1 == cur_one:
                        new_pos.append(new_pos_seg)
                        new_neg.append(new_neg_seg)
                        r = 0
                        k -= 1
                        new_pos_seg = Segment(0, [])
                        new_neg_seg = Segment(0, [])
                    else:
                        r += 1
                if new_pos_seg.values:
                    new_pos.append(new_pos_seg)
                    new_neg.append(new_neg_seg)
            pos = merge(new_pos)
            neg = merge(new_neg)
        assert pos
        assert pos[0].start == 0
        return pos[0].values[0]
    
    
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        print(solve(n))