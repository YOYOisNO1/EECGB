def program7008():
    text=input()
    ans=None
    for i in reversed(range(1,len(text))):
        if text[i]!=text[0]:continue
        if i<len(text)-i and text.startswith(text[i:]):
            ans=text[i:]
    if ans is not None:print('YES\n',ans,sep='')
    else:print('NO')