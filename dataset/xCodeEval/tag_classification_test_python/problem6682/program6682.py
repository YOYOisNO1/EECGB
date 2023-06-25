    a=input()+input()[::-1]
    b=input()+input()[::-1]
    s=set()
def dfs(state):
        if state in s:
            return
        s.add(state)
        for i in range(4):
            if state[i]=='X':
                for j in range(2):
                    a=(i+1)%4 if j else (i-1)%4
                    b=a+i
                    new=''
                    for k in range(4):
                        if k in (i, a):
                            new+=state[b-k]
                        else:
                            new+=state[k]
                    dfs(new)
                break
    dfs(a)
    print('YES') if b in s else 'NO'