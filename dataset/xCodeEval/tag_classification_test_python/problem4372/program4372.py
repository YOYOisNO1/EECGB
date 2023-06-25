def code(name):
        number =0
        number=min(ord(name[0])-ord('a'),ord('z')+1-ord(name[0]))
        iterator=1
        while iterator < len(name):
            temp1=min(ord(name[iterator]),ord(name[iterator-1]))
            temp2=max(ord(name[iterator]),ord(name[iterator-1]))
            temp3=abs(ord(name[iterator])-ord(name[iterator-1]))
            number=number+min(temp3,(ord('z')-temp2)+(temp1-ord('a')+1))
            iterator=iterator+1
        print(number)
    
    
    name = str(input()).lower()
    if len(name) in range(1,101):
    	code(name)
    else:
        print("NA")