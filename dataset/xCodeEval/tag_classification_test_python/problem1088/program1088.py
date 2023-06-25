def maxwin(a1,a2,a3,b1,b2,b3):
        return min(a1, b2) + min(a2, b3) + min(a3, b1)
    
def minwin(a1,a2,a3,b1,b2,b3):
        return max(0, b1 - a1 - a2) + max(0, b3 - a1 - a3) + max(0, b2 - a2 - a3)
    
    n = int(input())
    a1,a2,a3 = map(int, input().split())
    b1,b2,b3 = map(int, input().split())
    
    print(minwin(a1,a2,a3,b1,b2,b3), maxwin(a1,a2,a3,b1,b2,b3))