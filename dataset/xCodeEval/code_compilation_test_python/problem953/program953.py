def program953():
    s = input()
    vowels = ('aeiouy')  
    s = s.lower()
    result=''
    for x in s:
        if x in vowels:
           s = s.replace(x, “”)
        if x not in vowels:
            result=result+'.'
            result=result+x
    print(result)
            
            