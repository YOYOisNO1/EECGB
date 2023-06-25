    """
    Codeforces Contest 307 Div 2 Problem D
    
    Author  : chaotic_iak
    Language: Python 3.4.2
    """
    
    ################################################### SOLUTION
    
def multiply(M1, M2):
        if len(M1[0]) != len(M2): raise ValueError
        a = len(M1)
        b = len(M2[0])
        c = len(M1[0])
        # M1: a x c, M2: c x b, M: a x b
        ans = [[0]*b for _ in range(a)]
        for i in range(a):
            for j in range(b):
                for k in range(c):
                    ans[i][j] += M1[i][k] * M2[k][j]
        return ans
    
def solve(n, m):
        M = [[0,1,0],[1,1,0],[0,1,2]]
        if n == 0:
            return [[1,0,0],[0,1,0],[0,0,1]]
        if n == 1:
            return M
        P = solve(n//2, m)
        S = multiply(P, P)
        if n%2: S = multiply(S, M)
        for i in range(3):
            for j in range(3):
                S[i][j] = S[i][j] % m
        return S
    
def main():
        n,k,l,m = read()
        kb = bin(k)[2:]
        if l == 0 and k == 0: return 1 % m
        if len(kb) > l: return 0
        kb = "0" * (l - len(kb)) + kb
        zero, one = 0, 0
        for i in kb:
            if i == "0":
                zero += 1
            else:
                one += 1
    
        multiplier = solve(n, m)
        _, _, ans_one = multiply(multiplier, [[1],[0],[0]])
        multiplier = multiply(multiplier, solve(2, m))
        _, ans_zero, _ = multiply(multiplier, [[1],[0],[0]])
        return (pow(ans_zero[0], zero, m) * pow(ans_one[0], one, m)) % m
    
    
    
    #################################################### HELPERS
    
    
    
def read(mode=2):
        # 0: String
        # 1: List of strings
        # 2: List of integers
        inputs = input().strip()
        if mode == 0: return inputs
        if mode == 1: return inputs.split()
        if mode == 2: return list(map(int, inputs.split()))
    
def write(s="\n"):
        if s is None: s = ""
        if isinstance(s, list): s = " ".join(map(str, s))
        s = str(s)
        print(s, end="")
    
    write(main())