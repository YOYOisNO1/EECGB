    from sys import stdin, stdout, setrecursionlimit
    import threading
    
    # tail-recursion optimization
    # In case of tail-recusion optimized code, have to use python compiler.
    # Otherwise, memory limit may exceed.
    # declare the class Tail_Recursion_Optimization
    class Tail_Recursion_Optimization:
    def __init__(self, RECURSION_LIMIT, STACK_SIZE):
            setrecursionlimit(RECURSION_LIMIT)
            threading.stack_size(STACK_SIZE)
            return None
            
    class SOLVE:
    def DP(self, s, n, a, b):
            if len(s) == n:
                return 1
            
            total = 0
            for i in range(len(a)):
                if s[0] == b[i]:
                    total += self.DP(a[i]+s[1:], n, a, b)
                
            return total
        
    def solve(self):
            R = stdin.readline
            #f = open('input.txt');R = f.readline
            W = stdout.write
            
            n, q = [int(x) for x in R().split()]
            a, b = [None for i in range(q)], [None for i in range(q)]
            
            for i in range(q):
                a[i], b[i] = [x for x in R().split()]
            
            W('%d\n' % self.DP('a', n, a, b))
            return 0
            
def main():
        s = SOLVE()
        s.solve()
    #Tail_Recursion_Optimization(10**7, 2**26) # recursion-call size, stack-size in byte
    threading.Thread(target=main).start()
    #main()