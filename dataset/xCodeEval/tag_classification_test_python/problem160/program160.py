def program160():
    num = input("")
    count=0
    for i in num:
        if i == '4' or i == '7':
            count+=1
    
    ar_print_korbi_nah = False
    
    
    if count == 7 or count == 4:
        print("YES")
        ar_print_korbi_nah=True
    
    c_2=0
    
    
    for i in str(count):
     if (i == '7') or (i == '4'):
         c_2 += 1
    
    
    if (c_2 == len(str(count))) and ar_print_korbi_nah == False:
        print("YES")
    
    else:
        if ar_print_korbi_nah == False :
            print("NO")