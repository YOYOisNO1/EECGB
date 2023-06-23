def program2879():
    import re
    
    password = input()
    codes = {}
    
    for i in range(0, 10):
        code = input()
        codes[code]= i
    
    password = ""
    
    while len(password) < 8:
        for code in codes:
            if re.search("^"+code, password):
                password += codes[code]
    
    print(password)