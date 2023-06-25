    
def solve():
        n,k,d = list(map(int,input().split()))
        
        # ways n upto d-1 edges
        ways_small = [0 for _ in range(n+1)]
        for i in range(1,n+1,1):
            if i < d:
                ways_small[i] = 1
            
            for j in range(1,d,1):
                if i < j:
                    break
                ways_small[i] += ways_small[i-j]
                
        ways_large = [0 for _ in range(n+1)]
        for i in range(1,n+1,1):
            if i < k+1:
                ways_large[i] = 1
            
            for j in range(1,k+1,1):
                if i < j:
                    break
                ways_large[i] += ways_large[i-j]
        
        answer = (ways_large[n]-ways_small[n])%(1000000007)
        print(answer)
    if __name__ == "__main__":
        solve()