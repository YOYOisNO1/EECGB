def program228():
    
    random_string = input()
    '''i = 0
    h,e,l1,l2,o = -5,-5,-5,-5,-5
    for character in random_string:
        if character=='h':
            if (h == -5):
                h = i
        elif character == 'e':
            if (e ==-5):
                e = i
        elif character== 'l':
            if(l1 == -5):
                l1 = i
        elif character== 'o':
            if(o==-5):
                o = i
        if character== 'l':
            if(l1 != -5):
                l2 = i
        i = i+1
    if (h<e<l1<l2<o):
        print("YES")
    else:
        print("NO")
    #print(h, e, l1, l2, o)'''
    
    
    '''print('h' in random_string)
    print('e' in random_string)
    print('l' in random_string)
    print('l' in random_string)
    print('o' in random_string)'''
    
    i=0
    for h in random_string:
        if h=='h':
            break
        i = i + 1
    
     
    for e in random_string[i+1:]:
        i = i + 1
        if e=='e':
            break
    
     
    for l1 in random_string[i+1:]:
        i = i + 1
        if l1=='l':
            break
    
     
    for l2 in random_string[i+1:]:
        i = i + 1
        if l2=='l':
            break
    
     
    c=0
    for o in random_string[i+1:]:
        if o=='o':
            print("YES")
            c=1
            break
    if(c==0):
        print("NO")
    
    
    
    
    
    
    