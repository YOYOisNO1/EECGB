def largestDivisor(n):
        if (n==1):
            return 1
        i=n-1
        while i>=1:
            if (n%i==0):
                return i
            i-=1
def gameResult(n):
        points  = n
        while n>1:
            points = points +largestDivisor(n)
            n = largestDivisor(n)
        return points
    x = int(input())
    print(gameResult(x))