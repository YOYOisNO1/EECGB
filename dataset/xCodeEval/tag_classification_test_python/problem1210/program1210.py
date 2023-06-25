def program1210():
    for _ in range(int(input())):
        i,j=map(int,input().split())
        k,l=map(int,input().split())
        if (i==1 and l==1 and j==1 and k==1):
            print(2)
        else:
            if i==1 or j==1 or k==1 or l==1:
                print(1)
            else:
                print(0)
        