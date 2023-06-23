def mean(seq):
        N = len(seq)
        return sum(seq)/float(N)
        
def std(seq):
        m = mean(seq)
        N = len(seq)
        return sum([(s-m)**2/N for s in seq])
    
def solve(seq):
        m = mean(seq)
        s = std(seq)
        
        s1 = m
        s2 = m*(m+1)/3
        
        if abs(s-s1) < abs(s-s2):
            return int(m)
        else:
            return (max(seq)+1)/2
            
    V = int(input())
    seqs = [map(int, input().split()) for i in xrange(V)]
    
    for seq in seqs:
        print solve(seq)