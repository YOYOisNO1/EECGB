def program1114():
    n=int(input())
    ra,sa,pa=map(int,input().split())
    rb,sb,pb=map(int,input().split())
    maxa=min(ra,sb)+min(sa,pb)+min(pa,rb)
    rbsb,sbpb,pbrb=rb+sb,sb+pb,pb+rb
    l=[[ra,0],[sa,1],[pa,2]]
    l2=[rb,sb,pb]
    l3=[i[:] for i in l]
    l4=l2[:]
    l.sort(reverse=True)
    l3.sort()
    mina,mina2=0,0
    for i in l:
        pq=min(i[0],l2[i[1]])
        i[0]=max(0,i[0]-pq)
        l2[i[1]]=max(0,l2[i[1]]-pq)
        pq1=min(i[0],l2[(i[1]+2)%3])
        i[0]=max(0,i[0]-pq1)
        l2[(i[1]+2)%3]=max(0,l2[(i[1]+2)%3]-pq1)
        mina+=(pq1+pq)
    for i in l3:
        pq=min(i[0],l4[i[1]])
        i[0]=max(0,i[0]-pq)
        l4[i[1]]=max(0,l4[i[1]]-pq)
        pq1=min(i[0],l4[(i[1]+2)%3])
        i[0]=max(0,i[0]-pq1)
        l4[(i[1]+2)%3]=max(0,l4[(i[1]+2)%3]-pq1)
        mina2+=(pq1+pq)
    print(min(n-mina,n-mina2),maxa)