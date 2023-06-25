def check_code (a,b)
         for i in range (len(a)):
             if a[i] != b[len(b)-1-i]:
            return ("No")
        return ("Yes")
    
    
    a=input ()
    b=input ()
    if len(a)==len(b):
        print (check_code (a,b))
    else:
        print ("No")
       