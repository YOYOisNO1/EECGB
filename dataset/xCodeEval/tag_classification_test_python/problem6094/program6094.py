def program6094():
    s=input()
    r=int(s[:-1])-1
    print(r/4*16+r%2*7+'.fedabc'.index(s[-1]))