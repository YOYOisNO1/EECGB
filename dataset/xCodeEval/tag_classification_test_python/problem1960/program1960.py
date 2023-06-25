def program1960():
    n = input()
    a = input()
    b = input()
    k = n
    flag = 0
    count = 0
    while(n>=0):
        if(n%a==0):
            flag=1
            break
        else:
            count+=1
            n-=b
    
    if(flag==1):
        print("YES")
        y = count
        x = (k-(b*y))/a
        print(x,y)
        
    else:
        print("NO")