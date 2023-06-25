def program1223():
    string = input()
    while "dot" in string[1:-1]:
    	string = string[:string[1:].index("dot")+1]+"."+string[string[1:].index("dot")+4:]
    string = string[:string[1:].index("at")+1]+"@"+string[string[1:].index("at")+3:]
    print(string)