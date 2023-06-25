def minv(a, b):
        m = 0
        for i in range(3):
            m = max(m, b[i] - a[i] - a[(i+1)%3])
        return m
def maxv(a, b):
        total = 0
        for i in range(3):
            total += min(a[i], b[(i+1)%3])
        return total
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(minv(a, b), maxv(a, b))
    