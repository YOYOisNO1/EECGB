def program1607():
    ins=input()
    intt=input()
    l=len(ins)
    a=0
    for i in range(l):
        if ord(intt[i])-ord(ins[i])>=2:
            p=ord(ins[i])+1
            print ins[0:i]+chr(p)+ins[i+1:]
            a=1
            break
    if a!=1:
        print:'No such string'