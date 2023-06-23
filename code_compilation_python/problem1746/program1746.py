def program1746():
    x=input()
    y=input()
    i=1
    if x=="R":
        i*=-1
    key = "qwertyuiopasdfghjkl;zxcvbnm,./"
    s=""
    for m in y:
        s+=key[key.index(m)+i]:
    print s