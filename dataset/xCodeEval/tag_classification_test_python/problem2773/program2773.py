    t = int(input())
    
    limits = [
        sum(range(i, 10)) for i in range(1, 10)
    ][::-1]
    
def process(s):
        l = None
        for i, limit in enumerate(limits):
            if s <= limit:
                l = i + 1
                break
        s2 = limits[l - 1]
        nums = list(range(10 - l, 10))
        #print(nums)
        if s == s2:
            return nums
        for i in range(len(nums)):
            while nums[i] > i + 1:
                if s2 == s:
                    return nums
                nums[i] -= 1
                s2 -= 1
            if s2 == s:
                return nums
        return []
    
    
    for i in range(t):
        s = int(input())
        print(*process(s), sep='')