def program2240():
    n=int(input())
    inp = list(map(int,input().split()))
    sol=[]
    for i in range(n):
        for j in range(i+1,n):
            sol.append(abs(360-2*sum(inp[i:j])))
    print (min(sol))