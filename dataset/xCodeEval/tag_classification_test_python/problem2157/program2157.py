    num=input()
    n=int(num)
    b=0
def luckynumber(x):
        if x.count('4')+x.count('7')==len(x):
            return 1
        else:
            return 0
    if luckynumber(num)==1:
        print("YES")
        b=1
    else:
        for x in range(4,int(n/2+1)):
            if n%x==0 and luckynumber(str(x))==1:
                print("YES")
                b=1
                break
    if b==0:
        print("NO")