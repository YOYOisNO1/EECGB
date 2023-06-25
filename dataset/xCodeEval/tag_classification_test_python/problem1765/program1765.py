def program1765():
    for m in range(5):
        string=list(map(int,input().split()))
        k=1
        for n in string:
            if n==1:
                move=abs(k-3)+abs(m-2)
                break
            else:
                k=k+1
    print(move)
    
        