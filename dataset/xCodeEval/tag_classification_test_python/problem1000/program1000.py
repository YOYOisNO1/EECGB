    from itertools import permutations
    
def calc(a, b):
        if b[0]<=a[0] and a[1]<=b[1]:
            return a[1]-a[0]+1
        
        if a[0]<=b[0] and b[1]<=a[1]:
            return b[1]-b[0]+1
        
        return max(0, min(b[1]-a[0], a[1]-b[0])+1)
        
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans1, ans2 = n, 0
    
    for t1 in permutations(range(3)):
        alice = {}
        s = 0
        
        for i in range(3):
            if t1[i]==0:
                alice['r'] = [s, s+a[0]-1]
                s += a[0]
            elif t1[i]==1:
                alice['s'] = [s, s+a[1]-1]
                s += a[1]
            else:
                alice['p'] = [s, s+a[2]-1]
                s += a[2]
                
        for t2 in permutations(range(3)):
            bob = {}
            s = 0
            
            for i in range(3):
                if t2[i]==0:
                    bob['r'] = [s, s+b[0]-1]
                    s += b[0]
                elif t2[i]==1:
                    bob['s'] = [s, s+b[1]-1]
                    s += b[1]
                else:
                    bob['p'] = [s, s+b[2]-1]
                    s += b[2]
        
            win = calc(alice['r'], bob['s'])+calc(alice['s'], bob['p'])+calc(alice['p'], bob['r'])
            ans1 = min(ans1, win)
            ans2 = max(ans2, win)
    
    print(ans1, ans2)