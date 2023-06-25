    w, b = map(float, input().split())
    
    
    dp = {}
def solve(w, b, p, turn):
        #print(w,) b, p, turn
        key = (w, b, turn)
        if key in dp:
            return dp[key]
    
        if w == 0:
            return 0
    
        if b == 0:
            if turn:
                return p
            else:
                return 0
    
        result = 0
        if turn:
            wc =  p * (w / (w+b))
            bc = solve(w, b-1, p * (b / (w+b)), not turn)
            result = wc + bc
        else:
            if b == 1:
                result = solve(w-1, b-1, p * (b / (w+b)) * (w / (w+b-1)), not turn)
            else:
                result = solve(w-1, b-1, p * (b / (w+b)) * (w / (w+b-1)), not turn) + solve(w, b-2, p * (b / (w+b)) * ((b-1) / (w+b-1)), not turn)
    
    
        dp[key] = result
        return result
    
    print(solve(w,) b, 1, True)
    
    #for key in dp:
    #    print(key,) dp[key]