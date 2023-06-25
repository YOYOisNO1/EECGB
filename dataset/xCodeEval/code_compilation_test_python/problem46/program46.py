def program46():
    cups=input()
    medals=input()
    polki=input()
    cups=map(int,cups)
    cups=cups[0]+cups[1]+cups[2]
    medals=map(int,medals)
    medals=medals[0]+medals[1]+medals[2]
    a=[0,1][cups%5!=0]
    b=[0,1][medals%10!=0]
    c=cups/5
    d=medals/10
    if a+b+c+d<=polki:
    	print 'YES'
    else:
    	print 'NO'