    =input()
    ch1=ch[0]+ch[1]
    ch2=ch[3]+ch[4]
    a=int(ch1)
    b=int(ch2) 
    s=0
def pal(a,b):
        return (a==(b%10)*10+b//10)
    if pal(a,b):
        print(0)
    else:
        while pal(a,b)==False:
            s=s+1
            if b!=59 :
                b=b+1
            else :
                b=0
                if a!=23:
                    a=a+1
                else :
                    a=0
               
                
        print(s)