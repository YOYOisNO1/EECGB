    n, m, k = [int(i) for i in input().strip().split(" ")]
    
    
def check(t):
        a = t - k + 1
        b = t - n + k
        pillows = t
        if a > 1:
            pillows += (t - a) * (a + t - 1) // 2
        else:
            pillows += 1 - a + t * (t - 1) // 2
        if b > 1:
            pillows += (t - b) * (b + t - 1) // 2
        else:
            pillows += 1 - b + t * (t - 1) // 2
        return pillows <= m
    
    
    low = 1
    high = m
    
    while low < high:
        mid = low + (high-low+1)//2
        if check(mid):
            low = mid
        else:
            high = mid - 1
    print(low)
    
    
    