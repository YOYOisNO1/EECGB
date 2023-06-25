def program1813():
    l1=list(str(input()))
    l2=list(str(input()))
    l3=list(str(input()))
    l4=list(str(input()))
    c=[]
    if (len(l1)-2>=(2*(len(l2)-2)) and len(l1)-2>=(2*(len(l3)-2)) and len(l1)-2>=(2*(len(l4)-2))) or (len(l2)-2>=(2*(len(l1)-2)) and len(l3)-2>=(2*(len(l1)-2)) and len(l4)-2>=(2*(len(l1)-2))):
        c.append(1)
    else:
        c.append(0)
    if (len(l2)-2>=(2*(len(l1)-2)) and len(l2)-2>=(2*(len(l3)-2)) and len(l2)-2>=(2*(len(l4)-2))) or (len(l1)-2>=(2*(len(l2)-2)) and len(l3)-2>=(2*(len(l2)-2)) and len(l4)-2>=(2*(len(l2)-2))):
        c.append(1)
    else:
        c.append(0)
    if (len(l3)-2>=(2*(len(l2)-2)) and len(l3)-2>=(2*(len(l1)-2)) and len(l3)-2>=(2*(len(l4)-2))) or (len(l2)-2>=(2*(len(l3)-2)) and len(l1)-2>=(2*(len(l3)-2)) and len(l4)-2>=(2*(len(l3)-2))):
        c.append(1)
    else:
        c.append(0)
    if (len(l4)-2>=(2*(len(l2)-2)) and len(l4)-2>=(2*(len(l3)-2)) and len(l4)-2>=(2*(len(l1)-2))) or (len(l2)-2>=(2*(len(l4)-2)) and len(l3)-2>=(2*(len(l4)-2)) and len(l1)-2>=(2*(len(l4)-2))):
        c.append(1)
    else:
        c.append(0)
    d={0:"A",1:"B",2:"C",3:"D"}
    if c.count(1)>1 or c.count(1)==0:
        print("C")
    else:
        for j in range(4):
            if c[j]==1:
                print(d[j])