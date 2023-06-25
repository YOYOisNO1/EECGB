    import math
def solve(n):
        if n & (n-1) == 0 :
            return 1
        x = math.log2(n)
        return x + (n - x)
    
    if __name__ == '__main__'
    print(int(input()))