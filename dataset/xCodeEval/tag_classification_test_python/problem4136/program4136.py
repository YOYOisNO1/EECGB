def program4136():
    n=int(input())
    N=map(int,input().split())
    if n%2!=0 and N[0]%2!=0 and N[n-1]%2!=0:
        print("Yes")
    else:
        print("No")