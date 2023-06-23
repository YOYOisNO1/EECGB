def program261():
    n=int(input())
    ch=input()
    l=["a","e","u","i","o","y"]
    i=0
    while(i<len(ch)-1):
        if(ch[i] in l):
            if(ch[i+1] in l):
                ch=ch[:i+1]+ch[i+2:]
            else:
                i=i+1
    print(ch)