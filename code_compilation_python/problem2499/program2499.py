def ones(num):
    	return num.count('1')
def zeros(num):
    	return num.count('0')
# def split(num):
    
    
    
    x=int(input())
    y=bin(int(input(),2))
    O=ones(y[2:])
    Z=zeros(y[2:])
    if O!=Z:
    	print(1)
    	print(y[2:])
    else:
    	print(2)
     	print(y[2:3] +" " +y[3:])
    
    
    