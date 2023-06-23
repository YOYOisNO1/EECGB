def program2916():
    s = input()
    
    cache = ""
    output = ""
    for i in s:
        cache += i
        if cache == ".":
            output += "0"
            cache = ""
        elif cache == "-.":
            output += "1"
            cache = ""
        elif cache = "--":
            output += "2"
            cache = ""
    
    print(output)