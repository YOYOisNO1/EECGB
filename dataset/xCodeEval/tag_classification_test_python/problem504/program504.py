    import sys
    data = input().split(" ")
    n = int(data[0])
    k = int(data[1])
def works(n, k, v):
        lines = v
        total = 0;
        while lines>0:
            total += lines
            lines = lines/k
        if total>=n:
            return True
        else:
            return False
    low = 0
    high = n 
    while low<high-1:
        mid = (low+high) /2
        if works(n, k, mid):
            high = mid
        else:
            low = mid
    print(high)