def program2633():
    s=input ()
    a=-1
    c=0
    result=""
    
    for letter in s :
        if letter != "=" :
            a+=1
        else:
            break
    c= len(s) - 2 - a
    if c == a :
        result =s
    elif c-a == 2:
        result = s[-1] + s[0:-1]
    elif c-a == -2:
        if s[1] !="+":
            result = s[1:] + s[0]
        else:
            result = s[0:3] + s[4:] + s[0]
            
    else:
        result="Impossible"
    
    print((result))