    import sys
    
def solve():
        n = int(input())
        if n == 1: return 0
        res = 1000000
        for other in range(1, n):
            pair = [n, other]
            temp = 0
            while pair[0] > 1 or pair[1] > 1:
                if pair[0] > pair[1]: pair[0], pair[1] = pair[1], pair[0]
                pair[1] -= pair[0]
                temp+=1
            res = min(res, temp)
        return res
    
    
    
    if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
    print(solve())