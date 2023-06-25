def program4412():
    n=input()
    n=n[:1]+n[1:len(n)-1].replace('at','@',1)+n[len(n)-1:]
    n=n[:1]+n[1:len(n)-1].replace('dot','.')+n[len(n)-1:]
    print(n)