def program1184():
    s=input()
    t=input()
    
    kx=ord(s[0])-ord('a')+1
    ky=int(s[1])
    
    dx=ord(t[0])-ord('a')+1
    dy=int(t[1])
    
    path=[]
    while kx!=dx or ky!=dy:
        move=''
        if kx>dx:
            move='L'
            kx-=1
        elif kx<dx:
            move='R'
            kx+=1
        if ky>dy:
            move=move+'D'
            ky-=1
        elif ky<dy:
            move=move+'U'
            ky+=1
        path.append(move)
        
    print(len(path))
    for x in path:
        print(x)