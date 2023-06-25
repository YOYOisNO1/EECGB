def is_palindrome(s):
        return s == s[::-1]
    s=input("")
    y=len(s)-1
    x=0
    l=list(s)
    flag=0
    check=0
    if len(l)==2 and l[0]!=l[1]:
        l.insert(0,l[1])
        check=1
    while x<=y:
        if check==1:
            break
        if l[x]!=l[y]:
            if l[y-1]==l[x]:
                if x==0:
                    l.insert(0,l[y])
                    s3=''.join(l)
                    if is_palindrome(s3):
                        flag=1
                        break
                    else:
                        flag=2
                        break
                l.insert(x,l[y-1])
                flag=1
            elif l[y]==l[x+1]:
                l.insert(y+1,l[x])
                s3=''.join(l)
                    if is_palindrome(s3):
                        flag=1
                        break
                    else:
                        flag=2
                        break
                flag=1
            else:
                flag=2
                
            break
        x+=1
        y-=1
    if check==1:
        print ''.join(l)
    elif flag==0:
        s=str(''.join(l[0:len(l)/2]))+l[len(l)/2]
        if len(l)%2==0:
            l=l[0:len(l)/2]
        else:
            l=l[0:len(l)/2+1]
        l.reverse()
        s=s+str(''.join(l))
        print s
    elif flag==1:   
        s1=''.join(l)
        print s1
    elif flag==2:
        print "NA"
        