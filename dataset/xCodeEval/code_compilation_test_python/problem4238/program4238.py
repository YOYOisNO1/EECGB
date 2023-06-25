    from sys import stdin
    
def solve():
        p1, t1 = map(int, stdin.readline().split())
        p2, t2 = map(int, stdin.readline().split())
        h, s = map(int, stdin.readline().split())
    
        dp = [float('inf')] * h
        dp[0] = 0
    
        best_time = float('inf')
        for i in range(h):
            if dp[i] == float('inf'):
                continue
    
            r1, r2 = t1, t2
            time = dp[i]
            dmg = i
            while dmg < h:
                # fire together
                together_time = time + max(r1, r2)
                together_damage = dmg + p1 + p2 - s
                if together_damage >= h:
                    best_time = min(best_time, together_time)
                else:
                    dp[together_damage] = min(dp[together_damage], together_time)
    
                # fire one independently
                dt = min(r1, r2)
                r1 -= dt
                r2 -= dt
                time += dt
                if r1 != r2:
                    if not r1:
                        dmg += p1 - s
                        r1 = t1
                    else:
                        dmg += p2 - s
                        r2 = t2
                
            best_time = min(best_time, time)
        
        print(best_time)
    
    solve()