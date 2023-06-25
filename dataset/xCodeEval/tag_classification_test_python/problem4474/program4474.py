def main():
        n,k=map(long,input().split())
        l=map(str," ".join( input()).split())
        for i in xrange(n):
            l[i]=ord(l[i])-ord('a')+1
        l=list(set (l))
        l.sort()
        n=len(l)
        lop=0
        p=l[0]
        c=1
        j=1
        i=0
        while j<n:
                if l[j]-l[i]>1 and c<k:
                    p+=l[j]
                    c+=1
                    i=j
                    j+=1
                else:
                    j+=1
        
        if c<k:
            print(-1)
        else:
            print(p)
    main()