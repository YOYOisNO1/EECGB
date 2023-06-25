def program1950():
    n = int(input())
    string  = input()
    d = {'2':'2','3':'3','4':'322','5':'5','6':'35','7':'7','8':'2227','9':'3327'}
    ans = ''
    for i in string:
        if i!='0' and i!='1':
            ans+=d[i]
    ans = list(ans)
    ans.sort(reverse=True)
    print(''.join(ans))