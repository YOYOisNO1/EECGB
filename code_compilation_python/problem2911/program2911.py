def program2911():
    t=int(input))
    for_in range(t):
        n=int(input())
        res=''
        for i in range(9,0,-1):
            if n>=i:
                res=str(i)+res
                n-=i
        print(res)