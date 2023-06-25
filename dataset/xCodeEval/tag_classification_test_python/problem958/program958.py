def program958():
    n=int(input())
    
    r1,s1,p1=tuple([int(x) for x in input().split()])
    r2,s2,p2=tuple([int(x) for x in input().split()])
    
    resmax = min(r1,s2)+min(s1,p2)+min(p1,r2)
    #next line - maximum losing...
    #resmin = min(r1,p2)+min(s1,r2)+min(p1,s2)
    #fix. Rock does not win if either paper or scisors is shown.
    resmin = min(r1,n-s2)+min(s1,n-p2)+min(p1,n-r2)
    
    print(n-resmin, resmax)