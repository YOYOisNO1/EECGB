def program737():
    pa=[]
    for i in range(8):
        a=input()
        for j in a:
            pa.append(j)
    pb=pa[::-1]
    a=[11]
    b=[11]
    for i in range(8,16):
        if pa[i]=="W" and pa[i-8]==".":
            a.append(1)
        if pb[i]=="B" and pb[i-8]==".":
            b.append(1)
    
    for i in range(16,24):
        if pa[i]=="W" and pa[i-8]=="." and pa[i-16]==".":
            a.append(2)
        if pb[i]=="B" and pb[i-8]=="." and pb[i-16]==".":
            b.append(2)
    
    for i in range(24,32):
        if pa[i]=="W" and pa[i-8]=="." and pa[i-16]=="." and pa[i-24]==".":
            a.append(3)
        if pb[i]=="B" and pb[i-8]=="." and pb[i-16]=="." and pb[i-24]==".":
            b.append(3)
    
    for i in range(32,40):
        if pa[i]=="W" and pa[i-8]=="." and pa[i-16]=="." and pa[i-24]=="." and pa[i-32]==".":
            a.append(4)
        if pb[i]=="B" and pb[i-8]=="." and pb[i-16]=="." and pb[i-24]=="." and pb[i-32]==".":
            b.append(4)
    
    for i in range(40,48):
        if pa[i]=="W" and pa[i-8]=="." and pa[i-16]=="." and pa[i-24]=="." and pa[i-32]=="." and pa[i-40]:
            a.append(5)
        if pb[i]=="B" and pb[i-8]=="." and pb[i-16]=="." and pb[i-24]=="." and pb[i-32]=="." and pb[i-40]:
            b.append(5)
    
    for i in range(48,56):
        if pa[i]=="W" and pa[i-8]=="." and pa[i-16]=="." and pa[i-24]=="." and pa[i-32]=="." and pa[i-40] and pa[i-48]==".":
            a.append(6)
        if pb[i]=="B" and pb[i-8]=="." and pb[i-16]=="." and pb[i-24]=="." and pb[i-32]=="." and pb[i-40] and pb[i-48]==".":
            b.append(6)
    
    for i in range(56,64):
        if pa[i]=="W" and pa[i-8]=="." and pa[i-16]=="." and pa[i-24]=="." and pa[i-32]=="." and pa[i-40] and pa[i-48]=="." and pa[i-56]==".":
            a.append(7)
        if pb[i]=="B" and pb[i-8]=="." and pb[i-16]=="." and pb[i-24]=="." and pb[i-32]=="." and pb[i-40] and pb[i-48]=="." and pb[i-56]==".":
            b.append(7)
    
    if min(a)<=min(b):
        print("A")
    else:
        print("B")