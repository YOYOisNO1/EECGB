def program1010():
    input()
    k=list(map(int,input().rstrip().split()))
    l=list(map(int,input().rstrip().split()))
    a1=max(0,k[0]-l[0]-l[2],k[1]-l[1]-l[0],k[2]-l[2]-l[1])
    a2=min(k[0],l[1])+min(k[1],l[2])+min(k[2],l[0])
    print(a1,a2)