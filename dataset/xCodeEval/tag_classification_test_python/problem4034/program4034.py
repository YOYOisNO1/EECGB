def program4034():
    n=input()
    a=input()
    chess=map(int,a.split())
    chess.sort()
    x=1
    y=2
    odd=0
    even=0
    for i in chess:
    	odd+=max(x,i)-min(x,i)
    	even+=max(y,i)-min(y,i)
    	x+=2
    	y+=2
    	
    print(min(odd,even))