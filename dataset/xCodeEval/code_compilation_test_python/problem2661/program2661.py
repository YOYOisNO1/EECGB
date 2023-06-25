    useless=input().split()
    n=int(useless[1])
    list1=list(map(int,input().split()))
def find(d,lis):
        if d>=max(lis)-min(lis):
            return 0
        else:
            lis=sorted(lis)
            temp1=lis[1:]
            temp2=lis[:-1]
            return 1+min(find(d,temp1),find(d,temp2))
    
    print (find(n,list1))