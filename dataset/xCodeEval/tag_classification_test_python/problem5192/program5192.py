    nums = input().split()
    n = int(nums[0])
    ll = int(nums[1])
    rr = int(nums[2])
    
def f(x, memo):
        if x <= 1:
            return x
        if x in memo:
            return memo[x]
        memo[x] = 2 * f(x / 2, memo) + x % 2
        return memo[x]
    
def l(x, memo):
        if x <= 1:
            return 1
        if x in memo:
            return memo[x]
        memo[x] = 2 * l(x / 2, memo) + 1
        return memo[x]
    
    mf, ml = {}, {}
    
def g(x, ll, rr, mf, ml):
        glall = l(x, ml)
        if ll == 1 and rr == glall:
            ans = f(x, mf)
            return ans
        gl = l(x / 2, ml)
        ans = 0
        if ll <= gl and rr <= gl:
            ans = g(x/2, ll, rr, mf, ml)
        if ll <= gl and rr == gl + 1:
            ans = g(x/2, ll, gl, mf, ml) + x % 2
        if ll <= gl and rr > gl + 1:
            ans = g(x/2, ll, gl, mf, ml) + x % 2 + g(x/2, 1, rr - gl - 1, mf, ml)
        if ll == gl + 1 and rr == gl + 1:
            ans = x % 2
        if ll >= gl + 1 and rr > gl + 1:
            ans = x % 2 + g(x/2, 1, rr - gl - 1, mf, ml)
        if ll > gl + 1:
            ans = g(x/2, ll - gl - 1, rr - gl - 1, mf, ml)
        return ans
    
    print(g(n,) ll, rr, mf, ml)