def program2408():
    # cook your code here
    n = int(input())
    stri = input()
    
    temp1 = 0
    temp2 = 0
    
    ans1 = 0
    ans2 = 0
    
    count=0
    for i in stri:
        if(i=='('):
            temp1=0
            temp2=0
            count+=1
            continue
        elif(i==')'):
            temp1=0
            temp2=0
            count-=1
            continue
        
        elif(i=='_'):
            temp1=0
            temp2=0
        else:
            if(count==0):
                temp1+=1
                if(temp1>ans1):
                    ans1=temp1
            else:
                temp2 +=1
                if(temp2==1):
                    ans2+=1
    print(ans1,ans2)