def program1220():
    st = input()
    p=st[0]
    st=st[1:].replace("dot",".")
    st=p+st#print(st)
    if st[-1]=="." :
        st=st[:-1]+"dot"
    p=st[0]
    st=st[1:].replace("at","@",1)
    if st[-1]=="@" :
        st=st[:-1]+"at"
    print(p+st)