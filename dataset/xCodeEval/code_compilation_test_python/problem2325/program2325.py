def program2325():
    n=int(input())
    number=list(map(int,input().split()))
    number1=list(map(int,input().split()))\
    c=0
    for i in number:
        for j in number1:
            if ((i^j) in number) or ((i^j) in number1): 
                c=c+1
    if (c%2==0):
        print("Karen")
    else:
        print("Koyomi")