    
def func():
        n = int(input())
        nums = [int(i) for i in input().split(' ')]
    
        mx = max(nums)
        mn = min(nums)
        md = (mx + mn) / 2
        res = (mx - mn) // 2
    
        count = dict()
        for i in nums:
            if not count.get(i):
                count[i] = 0
            count[i] += 1
    
        if len(count) == 2:
            if md == int(md):
                return int(res)
            s = list(count.items())
            return int(abs(s[0][0] - s[1][0]))
    
        if md != int(md):
            return -1
        
        for i in nums:
            if i != mn and i != mx and i != md:
                return -1
        return res
    
    print(func())