def program580():
    input_string=input()
    str_len = len(input_string)
    
    upper=[i for i in input_string if i.isupper()]
    
    if len(upper)>str_len/2:
    	print(input_string.upper())
    else:
    	print(input_string.lower())	