def f(l):
        n,a,b = l   #n=circle, a=start, b=steps
        return 1+(a+b-1)%n
    
    l = list(map(int,input().split()))
    print(f(l))