    #   ==========     //\\       //||     ||====//||
    #       ||        //  \\        ||     ||   // ||
    #       ||       //====\\       ||     ||  //  ||
    #       ||      //      \\      ||     || //   ||
    #   ========== //        \\  ========  ||//====|| 
    #  code
    
def solve():
        from itertools import permutations as perm
    
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
    
        maxans = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
        minans = 1e18
    
        k = [(0,0), (0,2), (1,1), (1,0), (2,1), (2,2)]
        k = perm(k)
    
        '''
        a0 b0
        a0 b2
        a1 b1
        a1 b0
        a2 b1
        a2 b2
        '''
    
        for i in k:
            aa = a[:]
            bb = b[:]
    
            for j in range(6):
                u = i[j][0]
                v = i[j][1]
    
                val = min(aa[u], bb[v])
                aa[u] -= val
                bb[v] -= val
            
            # print(aa , bb)
            
            ans = min(aa[0], bb[1]) + min(aa[1], bb[2]) + min(aa[2], bb[0])
            minans = min(minans, ans)
        print(minans, maxans)
        return
    
def main():
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()
    
    if __name__ == "__main__":
        main()