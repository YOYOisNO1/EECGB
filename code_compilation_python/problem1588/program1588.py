def program1588():
    a,b=[int(x) for x in input().split()]
    count=0
    if(b>a):
        while(a<b):
            a=a*2
            count+=1
        if(a==b):
            print(count)
        else:
             a=a/2
            print(count-1+b%a)
    
           
    else:
        print(a-b)
    
    