def program538():
    import re
    a=input()
    b=input()
    
    c=int(a)+int(b)
    c=re.sub('0','',str(c))
    
    a=re.sub('0','',a)
    b=re.sub('0','',b)
    
    c1=int(a)+int(b)
    
    if(int(c)==c1):
        print("YES")
    else:
        print("NO")