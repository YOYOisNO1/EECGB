def program3514():
    """
    Solution to Codeforces Problem 119A : https://codeforces.com/problemset/problem/119/A
    
    Difficulty: 800
    """
    import math
    s=lambda a,b,n,i:s(b,a,n-math.gcd(a,n),i+1)if n!=0else i%2
    print(s(*list(map(int,input().split(' '))),1))