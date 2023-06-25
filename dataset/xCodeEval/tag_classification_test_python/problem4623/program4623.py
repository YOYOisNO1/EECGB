def program4623():
    n,k=map(int,input().split())
    s=input()
    flag=False
    last_pos={}
    gate=set()
    for i in range(len(s)):
        last_pos[s[i]]=i
    #print(last_pos)
    for i in range(len(s)):
        gate.add(s[i])
        if len(gate)>k:
            flag=True
            break
        if last_pos[s[i]]==i:
            gate.remove(s[i])
    if flag:
        print('YES')
    else:
        print('NO')