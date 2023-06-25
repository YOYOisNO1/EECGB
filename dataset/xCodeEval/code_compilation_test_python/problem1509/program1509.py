def program1509():
    p=input()
    str1=""
    suma=0
    for i in p:
        if i==">":
            str1+="1000"
        elif i=="<":
            str1+="1001"
        elif i=="+":
            str1+="1010"
        elif i=="-":
            str1+="1011"
        elif i==".":
            str1+="1100"
        elif i==",":
            str1+="1101"
        elif i=="[":
            str1+="1110"
        elif i=="]":
            str1+="1111"
    
    for j in range(0,len(str1)):
        if str1[j]=="1":
            suma+=(2**(len(str1)-1-j))*1
    while suma>1000003:
        suma-=1000003
    print suma
            
        