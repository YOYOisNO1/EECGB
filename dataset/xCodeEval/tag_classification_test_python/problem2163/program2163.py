def program2163():
    a,b,c = input().partition('tp')
    d,e,f = c.rpartition('ru')
    if f: e+='/'
    print(a+b+'://'+d+'.'+e+f)