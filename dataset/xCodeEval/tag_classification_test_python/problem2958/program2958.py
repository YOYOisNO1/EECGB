def program2958():
    inp=input()
    if inp[1:].isupper() and inp[0].islower():
        print(inp[0].upper()) + inp[1:].lower()
    elif inp.isupper() :
        print(inp.lower())
    elif len(inp)==1:
        print(inp.upper())
    else:
        print(inp)