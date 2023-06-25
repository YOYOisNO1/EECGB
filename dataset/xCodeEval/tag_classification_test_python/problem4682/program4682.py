    import heapq
    
def doIt(s):
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if c in s:
                a,b = s.rfind(c), s.find(c)
                heapq.heappush(end, a)
                heapq.heappush(start, b)
        
        current = 0
        while start:
            if start[0] <= end[0]:
                heapq.heappop(start)
                current += 1
                
                if current > k:
                    return "YES"
            else:
                heapq.heappop(end)
                current -= 1
        return "NO"
    
    n,k = map(int, input().split())
    s = input()
    
    start = []
    end = []
    
    print(doIt(s))