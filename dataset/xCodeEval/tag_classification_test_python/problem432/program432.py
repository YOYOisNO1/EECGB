def program432():
    A=[int(i) for i in input().split()]
    B=[int(i) for i in input().split()]
    n=int(input())
    if sum(A)%5!=0:
        n-=(sum(A)//5+1)
    else:
        n-=sum(A)//5
    if sum(B)%10!=0:
        n-=(sum(B)//10+1)
    else:
        n-=sum(B)//10
    if n>=0:
        print("YES")
    else:
        print("NO")