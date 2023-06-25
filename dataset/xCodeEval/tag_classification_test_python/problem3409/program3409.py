def program3409():
    n=int(input())
    l=list(map(int,input().split()))
    x=[l[i+1] - l[i] for i in range(n-1)]
    y=[l[i+2] - l[i] for i in range(n-2)]
    print(max(max(x),min(y)))