def program3123():
    =int(input())
    s=input()
    ones=0
    newn=1
    ans=""
    i=0
    
    while(i<n):
        if(s[i]=="1"):
            j=i+1
            ones=1
            while(j<n and s[j]=="1"):
                ones+=1
                j+=1
            ans+=str(ones)
            i=j
        else:
            z=1
            j=i+1
            while(j<n and s[j]=="0"):
                z+=1
                j+=1
            if z>1:
                for k in range(0,z,2):
                    ans+="0"
            i=j
    print(ans)