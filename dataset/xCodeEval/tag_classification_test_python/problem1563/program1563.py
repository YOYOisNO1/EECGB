def program1563():
    import math
    #q=int(input())
    q=1
    for _ in range(q):
        s=(input())
        t=(input())
        n=len(s)
        ans=""
        flag=False
        for i in range(n):
            if s[i]==t[i]:
                ans+=s[i]
                continue
            elif ord(t[i])-ord(s[i])>1:
                ans+=(chr(ord(s[i])+1))
                k=(s[i+1:n])
                if len(k)!=0:
                    ans+=(k)
                flag=True
                print(ans)
                break
            else:
                ans1=ans
                ans+=s[i]
                for j in range(i+1,n):
                    if s[j]!='z':
                        ans+=(chr(ord(s[j])+1))
                        k=(s[j+1:n])
                        if len(k)!=0:
                            ans+=(k)
                        flag=True
                        break
                if flag:
                    print(ans)
                    break
                else:
                    flag=0
                    ans1+=chr(ord(s[i])+1)
                    for j in range(i+1,n):
                        ans1+='a'
                    for j in range(i+1,n):
                        if ord('a')<ord(t[j]):
                            flag=1
                            break
                    if flag==1:    
                        print(ans1)
                    else:
                        print("No such string")
                    break
                    
        