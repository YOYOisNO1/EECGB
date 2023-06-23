def program385():
    n1, n2, n3, n4, n5, n6 = input()
    n1= int(n1)
    n2= int(n2)
    n3= int(n3)
    n4= int(n4)
    n5= int(n5)
    n6= int(n6)
    
    if n1+n2+n3==n4+n5+n6:
        print("YES")
        
    elif n1+n2+n4==n3+n5+n6:
        print("YES")
    
    elif n1+n2+n5==n3+n4+n6:
        print("YES")
    
    elif n1+n2+n6==n3+n4+n5:
        print("YES")
        
    elif n1+n3+n4=n2+n5+n6:
        print("YES")
        
    elif n1+n3+n5==n2+n4+n6:
        print("YES")
        
    elif n1+n3+n6==n2+n4+n5:
        print("YES")
        
    elif n1+n4+n5==n2+n3=n6:
        print("YES")
        
    elif n1+n4+n6==n2+n3+n5:
        print("YES")
        
    elif n1+n5+n6==n2+n3+n4:
        print("YES")
        
    
    
    else:
        print("NO")