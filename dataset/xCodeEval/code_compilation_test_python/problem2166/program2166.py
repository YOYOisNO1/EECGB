def program2166():
    A,B,C=map(int,input().split())
    x=max(A,B,C)
    print(max(0,x-(A+B+C-x+1)