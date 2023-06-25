 def getI(a, k):
    
    def getSliceSum(ar, till):
            res = 0
            for i in range(till):
                res += ar[i]
            return res
        
        if k ==0: return 0
        if a[0] >=k: return 1
        count = 0
        a.sort(reverse=True)
        for ai in range(12):
            res = getSliceSum(a, ai)
            if res >= k: return ai