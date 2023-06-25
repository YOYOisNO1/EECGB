def program1006():
    """
    for _ in range(int(input())):
        m,n=map(int,input().split())
        l=[]
        for _ in range(m):
            l.append(list(map(int,input().split())))
        i=0
        j=m-1
        while i<j :
            if l[i]==l[j]:
                if ''.join(map(str,l[i]))[::-1]==''.join(map(str,l[i])) and ''.join(map(str,l[j]))[::-1]==''.join(map(str,l[j])):
                    i+=1
                    j-=1
                else:
                    break
            else:
                break
        if j<=i:
            print(0)
            continue
        else:  
        #print(l)
            a=[]
            for e in l:
                a.extend(e)
            l=a
            s=sum(l)//(m*n)
            count1=0
            for e in l:
                count1+=abs(s-e)
            count2=0
            for e in l:
                count2+=abs(s+1-e)
    
            print(min(count1,count2))
    """
    r=input()
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c1=min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0])
    l=[[0,0],[1,1],[2,2],[0,2],[1,0],[2,1]]
    c2=2**32
    
    from itertools import permutations
    import copy
    
    l=permutations(l)
    perm=[]
    for e in l:
        a1=copy.deepcopy(a)
        b1=copy.deepcopy(b)
        for ele in e:
            x=ele[0]
            y=ele[1]
            cnt=min(a1[x],b1[y])
            a1[x]-=cnt
            b1[y]-=cnt
        ans=min(a1[0],b1[1])+min(a1[1],b1[2])+min(a1[2],b1[0])
        c2=min(c2,ans)
    
    print(f'{c2} {c1}')