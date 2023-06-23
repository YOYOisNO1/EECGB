def program1701():
    d={"q":9,"r":5,"b":3,"n":3,"p":1,"k":0,"Q":9,"R":5,"B":3,"N":3,"P":1,"K":0}
    f={"m":0,"z":0}
    for k in range(8):
        a=input()
        for j in a:
            if(j!="." and j in "qprbnk"):
                f["z"]+=d[j]
            if(j!="." and j in "QRBNKP):
                f["m"]+=d[j]
    if(f["m"]>f["z"]):
        print("White")
    elif(f["m"]==f["z"]):
        print("Draw")
    else:
        print("Black")
                
            