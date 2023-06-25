    import math
def solve(n,l,r):
        ans = 0
        lb = list(map(int,bin(n)[2:]))
        for i in range(l,r+1):
            ans += lb[int(math.log2(i&-i))]
        return ans
    
    if __name__ == "__main__":
        n,l,r = map(int,input().split(" "))
        print(solve(n,l,r))