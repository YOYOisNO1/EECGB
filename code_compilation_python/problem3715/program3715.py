def rec_pie(pies):
        if len(pies) == 1:
            return pies[0]
        return max(rec_pie(pies[1:]), sum(pies) - rec_pie(pies[1:]))
        
    n = int(input())
    pies = [int(x) for x in input().split()]
    
    s = sum(pies)
    
    res = rec_pie(pies)
    
    print(s - res, res)