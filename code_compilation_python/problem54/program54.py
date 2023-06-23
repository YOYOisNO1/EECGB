    # cook your dish here
def S(x):
        ss=0
        while x:
            ss+=x%10
            x=x//10
        return ss
    
    n=input()
    s=""
    s=s+"9"*(len(n)-1)
    if n[0]=='9':
        s="9"+s
    else:
        s=chr(ord(n[0])-1)+s
    print(S(int(s))+S(int(n)-int(s)))