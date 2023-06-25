    dp = {}
def prob(w, b):
        if (w, b) in dp:
            return dp[(w, b)]
        if w == 0 and b == 0:
            return 0
        if b == 0:
            return 1
        if w == 0:
            return 0
        if b == 1:
            ans = w / (w + b)
            dp[(w, b)] = ans
            return ans
        if b == 2:
            ans = w / (w + 2) + 2 / (w + 2) * 1 / (w + 1) * prob(w - 1, b - 2)
            dp [(w, b)] = ans
            return ans
        sum = w + b
        if sum == 1 or sum == 2:
            print(w, b)
        ans = w / sum + (b / sum) * (b - 1) / (sum - 1) * (w / (sum - 2) * prob(w - 1, b - 2) + (b - 2) / (sum - 2) * prob(w, b - 3))
        dp[(w, b)] = ans
        return ans
    
    
    if __name__ == '__main__':
        w, b = tuple(map(int, input().split()))
        print(prob(w, b))