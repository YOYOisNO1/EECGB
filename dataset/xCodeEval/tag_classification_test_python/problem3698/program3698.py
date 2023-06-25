    s=input()
    a=b=0
    while(s[len(s)-1]=="0"):
        s=s[0:len(s)-1]
        a=a+1
    while(s[0]=="0"):
        s=s[1:len(s) ]
        b=b+1
def pa(s):
        if len(s)<=1:return True
        if s[0]==s[len(s)-1]:
            s=s[1:len(s)-1]
            return True and pa(s)
        return False
    print("YES") if (pa(s) and a>=b) else "NO"