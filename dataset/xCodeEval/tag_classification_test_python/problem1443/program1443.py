def program1443():
    
    n_and_m=input().split()
    n=int(n_and_m[0])
    m=int(n_and_m[1])
    colored=0
    black_and_white=0
    for i in range(n):
        c=list(map(str,input().split()))
        for j in c:
            if j in ['C','M' ,'Y']:
                colored+=1
            elif j in ['B','G','W']:
                black_and_white+=1
    if colored==n*m:
        print("#Color")
    elif black_and_white==n*m:
        print("#Black&White")
    else:
        if colored<n*m:
            print("#Color")
        else:
            print("#Black&White")