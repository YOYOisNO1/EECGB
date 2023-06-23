def program3528():
    import itertools
    ans=10000000000000
    n=map(int, input().split())
    x=map(str, input().split())
    nl=list(itertools.permutations(n))
    xl=list(itertools.permutations(x))
    nl=set(nl); nl=list(nl)
    xl=set(xl); xl=list(xl)
    
    for i in range(len(nl)):
        for j in range(len(xl)):
            e='(('+nl[i][0]+xl[j][0]+nl[i][1]+')'+xl[j][1]+nl[i][2]+')'+xl[j][2]+nl[i][3]
            f='('+nl[i][0]+xl[j][0]+nl[i][1]+')'+xl[j][1]+'('+nl[i][2]+xl[j][2]+nl[i][3]+')'
            ans=min(ans,eval(e),eval(f))
    print ans