    n=input()
    lst=[]
    for i in range(0,n):
        x=input()
        lst.append(x)
    s=0
    ans=[]
    
def meetinmiddle(lst,i,s=0):
        global n
        if i==n:
            ans.append(s)
        else:
            meetinmiddle(lst,i+1,(s+lst[i])%360)
            meetinmiddle(lst,i+1,(s-lst[i])%360)
    meetinmiddle(lst,0,0)
    if 0 in ans :
        print("yes")
    else:
        print("no")