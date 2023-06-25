def program50():
    
    N = int(input())
    x = map(int,input().strip('\n').split(' '))
    y = map(int,input().strip('\n').split(' '))
    if(sum(x)>=sum(y)):
    	print("Yes")
    else:
    	print("No")