def program1886():
    i = input().split()
    n,k = int(i[0]),int(i[1])
    if k <= (n+1)//2:
        print((k*2)-1)
    else:
        print(int(((k-((n+1)//2))*2)))