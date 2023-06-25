def program5456():
    n=int(input())
    m=list(input().split())
    if int(m[1])+int(m[0])<=n+1:
        print('White')
    else:
        print('Black')