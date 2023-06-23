def program743():
    s = input()
    x = ["Danil", "Olya", "Slava", "Ann","Nikita".]
    ans = [0]*5
    for i in range(len(x)):
        if x[i] in s:
            ans[i] += 1
    su = sum(ans)
    if su==1:
        fr = x[ans.index(1)]
        s = s.replace(fr,'')
        ans = [0]*5
        for i in range(len(x)):
            if x[i] in s:
                ans[i] += 1
        if sum(ans)!=0:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')