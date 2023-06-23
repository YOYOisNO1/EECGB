def program4272():
    x=input()
    x=int(x)
    temp=[]
    for i in range(0,x):
        y=input()
        temp.append(int(y))
    check = temp[1]-temp[0]
    conunter=0
    for i in range (1,len(temp)-1):
        if temp[i+1]-temp[i]== check:
            conunter= conunter +1
    if conunter== (len(temp)-2):
        print(temp[len(temp)-1]+check)
    else:
        print(temp[len(temp)-1])