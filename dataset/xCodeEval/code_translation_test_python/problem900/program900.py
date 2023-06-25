def program900():
    import math
    n=int(input())
    res=0
    for a in range(1,n):
        for b in range(1,n):
            c = math.sqrt(a*a+b*b)
            if(int(c)==c and c<=n):
                res+=1
    print(res//2)