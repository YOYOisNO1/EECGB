    import math
def log(n):
        i = 0
        while n > 0:
            i = i + 1
            n = n//2
        return i
            
def length(n):
        if n == 0:
            return 1
        a = log(n)
        return 2**a - 1
     
def solve(n,left,right):
        l = length(n)
        middle = (l + 1)//2
        if n == 1:
            return 1
        if n == 0:
            return 0
        if left > right:
            return 0
        half,rem = divmod(n,2)
        if middle == right and middle == left:
            return rem
        elif middle >= right :
            if middle == right:
                return solve(half,left,middle-1) + rem
            else:
                return solve(half,left,right)
        elif left >= middle:
            if middle == left:
                return solve(half,1,right - middle) + rem
            else:
                return solve(half,left - middle,right - middle)
        else:
            return solve(half,left,middle -1) + solve(half,1,right - middle) + rem
            
     
     
    a1,a2,a3 = [int(x) for x in input().split()]
    print(solve(a1,a2,a3))