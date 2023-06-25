def program4223():
    import re
    n=int(input())
    s=input()
    a=re.search('000',s)
    #print(a)
    b=re.search('11',s)
    #print(a,b)
    if s=='0':
        print("NO")
    elif s=='00':
        print("NO")
    elif s[-2:]=='00':
        print("NO")
    elif s[:2]=='00':
        print("NO")
    else:
        if a or b:
            print("NO")
        else:
            
            print("YES")
    