def solve():
        digits = [0]*10
        n = list(input().strip())
        for i in n:
            digits[int(i)] += 1
        m = list(input().strip())
        if len(n)!=len(m):
            return 1
        prev = 0
        for i in xrange(1,10):
            if digits[i]!=0:
                if m[0] != str(i):
                    return 1
                digits[i] -= 1
                m.pop(0)
                break
        for i in m:
            if i>=prev:
                digits[int(i)] -= 1
                prev = i
            else:
                return 1
        for i in digits:
            if i!=0:
                return 1
        return 0
    
    x = ['OK', 'WRONG_ANSWER']
    print(x[solve()])