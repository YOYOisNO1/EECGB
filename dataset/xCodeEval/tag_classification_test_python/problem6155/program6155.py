def program6155():
    s=input()
    s=s.split()
    for i in range(4):
        s[i]=int(s[i])
        
    x1=s[0]
    y1=s[1]
    x2=s[2]
    y2=s[3]
    
    #bishop
    if((abs(x1-x2)+abs(y1-y2))%2!=0):
        ansbishop=0
    elif (abs(x1-x2)==abs(y1-y2)):
        ansbishop=1
    else:
        ansbishop=2
    #rook
    if(x1==x2 or y1==y2):
        ansrook=1
    else:
        ansrook=2
    # ansrook=abs(x1-x2)+abs(y1-y2)
    #king
    s=abs(min((x2-x1),(y2-y1)))
    ansking=max(abs(x1-x2),abs(y1-y2))
    print(str(ansrook)+") "+str(ansbishop)+" "+str(ansking)