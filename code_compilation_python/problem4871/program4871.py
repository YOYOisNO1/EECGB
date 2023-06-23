    n,m,capacity = [int(x) for x in input().split()]
    
    class Planet:
    def __init__(self):
            self.a = []
            self.b = []
            self.c = []
            self.n = ""
    def __repr__(self):
            return "%s: a:%r, b:%r, c:%r" % (self.n, self.a, self.b,self.c)
    
def calc_profit(p1, p2):
        #print "%s -> %s" % (p1.n, p2.n)
        profits = []
        for j in range(m):
            if p1.c[j] == 0:
                continue
            profit = p2.b[j] - p1.a[j]
            if profit > 0:
                profits.append((profit, p1.c[j]))
        profits.sort(reverse=True)
        load = 0
        total_profit = 0
        for p in profits:
            if load + p[1] > capacity:
                c = capacity - load
            else: 
                c = p[1]
            total_profit += p[0]*c
            load += c
            if c != p[1]:
                break
        #print "profit: %d" % total_profit
        return total_profit 
    
    ps = []
    
    for i in range(n):
        p = Planet()
        p.n = input()
        for j in range(n):
            a,b,c = [int(x) for x in input().split()]
            p.a.append(a)
            p.b.append(b)
            p.c.append(c)
        ps.append(p)                  
        
    max_profit = -1
    
    for n1 in range(n):
        for n2 in range(n):
            if n1 != n2:
                profit = calc_profit(ps[n1], ps[n2])
                max_profit = max(max_profit, profit)
    
    print max_profit        