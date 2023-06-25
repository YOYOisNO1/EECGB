def program3025():
    s = input()
    
    ans = ['','','','','','','','','','']
    ansnum = 0
    for i in s:
        cur = ord(i) - ord('0')
        ansnum = max(ansnum,cur)
    
    print(ansnum)
    for i in s:
        cur = ord(i) - ord('0')
        for j in range(cur):
            ans[j]+='1'
        for j in range(cur,ansnum):
            ans[j]+='0'
    
    for i in range(ansnum):
        print(int(ans[i]),'\r',)