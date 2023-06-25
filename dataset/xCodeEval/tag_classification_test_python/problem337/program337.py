    from functools import reduce
    n=int(input().strip())
    l=[0]+list(map(int,input().strip().split()))
def check(l,n):
        required=reduce(lambda x,y:x+y,l)//2+1
        seats=l[1]
        if l[1]>=required:
            print(1)
            print(1)
            return 0
        i=2
        indexes=[1]
        while i<=n and seats<=required:
            if 2*l[i]<=l[1]:
                indexes.append(i)
                seats+=l[i]
            i+=1
        if seats>=required:
            print(len(indexes))
            for i in range(len(indexes)):
                print(indexes[i],end=" ")
        else:
            print(0)
    check(l,n)