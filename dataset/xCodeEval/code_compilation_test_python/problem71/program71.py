def program71():
    x=int(input())
    a,b,c=map(int,input().split())
    A=[a,b,c]
    if A[x-1]!=0 and A[A[x-1]]!=0:
        print("YES")
    else:
        print("NO")