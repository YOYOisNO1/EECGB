    n=int(input())
def mod(a):
        if(a<0):
            return -1*a
        else:
            return a
    lst=[int(e) for e in input().split()]
    s=set(lst)
    if(len(s)==1):
        print("0")
    elif(len(s)>3):
        print("-1")
    elif(len(s)==2):
        l1=list(s)
        if(mod(l1[1]-l1[0])%2!=0):
            print(mod(l1[1]-l1[0]))
        else:
            print(mod(l1[1]-l1[0])//2)
    else:
        l=list(s)
        l.sort()
        if(l[2]-l[1]==l[1]-l[0]):
            print(l[2]-l[1])
        else:
            print("-1")