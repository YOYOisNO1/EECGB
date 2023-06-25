    import heapq as hp
    import math
    
    
def primeSeive(n):
        """return prime numbers <=n"""
        l = [True] * (n + 1)
        l[0] = l[1] = False
        l[2] = l[3] = True
        for i in range(4, n + 1, 2):
            l[i] = False
        for i in range(9, n + 1, 3):
            l[i] = False
        for i in range(10, n + 1, 5):
            l[i] = False
        for i in range(7, int(math.sqrt(n)) + 1, 2):
            if l[i]:
                for j in range(i * i, n + 1, i):
                    l[j] = False
        return [i for i in range(n + 1) if l[i]]
    
    
def unpack(func=int):
        return map(func, input().split())
    
    
def range_n():
        return range(int(input()))
    
    
def main():
        n = int(input())
        ans=0
        while n>1:
            k=n-2*(n//2)
            ans+=k
            n-=k
            n//=2
        ans+=n
        print(ans)
    
    main()