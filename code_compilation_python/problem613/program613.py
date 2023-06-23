def program613():
    include math
    ent=input()
    a,b,c,d=ent.split()
    print(math.ceil((a*math.ceil(b/c))/d))