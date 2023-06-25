def program481():
    import re
    s=input()
    d=re.findall(r'\d+',s)
    tiles=(2**(int(d[0])+int(d[1])))%998244353
    print(tiles)