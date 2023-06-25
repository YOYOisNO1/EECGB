def program1432():
    n=int(input())+1;p=0
    a=sum(list(map(int,input().split())))
    for i in range(1,6):
    	if (a+i)%n!=1:p+=1
    print(p)