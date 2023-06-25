    from collections import defaultdict as ddic, deque, Counter
    from itertools import combinations, permutations, product
    import sys
    sys.setrecursionlimit(10**6)
    stdout = sys.stdout
    rr = lambda: input().strip()
    rri = lambda: int(input())
    rrm = lambda: list(map(int, input().strip().split()))
    
    from fractions import gcd
def solve(M, A, B):
        # x -> x+a or x-b
        g = gcd(A, B)
        reachable = [True]
        S = 1
        ans = 1
        for x in xrange(1, 1 + min(M, A+B-1) ):
            if x-A >= 0 and reachable[x - A]:
                reachable.append(True); S+=1
                if x-B >= 0 and not reachable[x-B]:
                    queue = deque([x-B])
                    reachable[x-B] = True; S+=1
                    while queue:
                        node = queue.popleft()
                        if node + A < len(reachable) and not reachable[node+A]:
                            reachable[node+A] = True; S+=1
                            queue.append(node+A)
                        if node - B >= 0 and not reachable[node-B]:
                            reachable[node-B] = True; S+=1
                            queue.append(node-B)
            else:
                reachable.append(False)
    
            ans += S
        
    def sumtoN(N):
            return N * (N+1) // 2
    
        # Now to count x = A+B... M
        # ans += sum( 1 + x // g for x in xrange(A+B, M+1))
        todo = M - (A+B) + 1
        if todo < 1: return ans
        bns = 0
        bns += todo
        # ans += sum(x//g for x in A+B ... M)
        base = (A+B) // g
        # base * g + (base+1) * g + ... + (base + q - 1) * g + (base + q) * r
        q, r = divmod(M -(A+B) + 1, g)
    
        bns += g * ( sumtoN(base+q-1) - sumtoN(base-1) )
        bns += (base+q) * r
    
        ans += bns
        return ans
        
                
    
    print(solve(*rrm()))