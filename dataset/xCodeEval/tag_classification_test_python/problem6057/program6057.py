    rook=input()
    k=input()
    blocked=[str(rook[0]+str(i)) for i in range(1,9)]+[str(chr(96+i)+str(rook[1])) for i in range(1,9)]+[rook+k]
    kn=[
        chr(ord(k[0])-1)+str(int(k[1])+2),
        chr(ord(k[0])-1)+str(int(k[1])-2),
        chr(ord(k[0])+1)+str(int(k[1])+2),
        chr(ord(k[0])+1)+str(int(k[1])-2),
        chr(ord(k[0])-2)+str(int(k[1])+1),
        chr(ord(k[0])-2)+str(int(k[1])-1),
        chr(ord(k[0])+2)+str(int(k[1])+1),
        chr(ord(k[0])+2)+str(int(k[1])-1),
        chr(ord(rook[0])-1)+str(int(rook[1])+2),
        chr(ord(rook[0])-1)+str(int(rook[1])-2),
        chr(ord(rook[0])+1)+str(int(rook[1])+2),
        chr(ord(rook[0])+1)+str(int(rook[1])-2),
        chr(ord(rook[0])-2)+str(int(rook[1])+1),
        chr(ord(rook[0])-2)+str(int(rook[1])-1),
        chr(ord(rook[0])+2)+str(int(rook[1])+1),
        chr(ord(rook[0])+2)+str(int(rook[1])-1)
    ]
def verify(s):
        if len(s)>2: return False
        n=int(s[1])
        if ('a'<=s[0]<='h') and (1<=n<=8): return True
        return False
    for i in kn:
        if verify(i): blocked.append(i)
    
    blocked = list(set(blocked))
    print(64-len(blocked))