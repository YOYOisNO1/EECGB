def program3521():
    myDict = {
        "3" : "the",
        "5" : "buffy",
        "6" : "slayer",
        "7" : "vampire",
    }
    s = input("").strip()
    if len(s) == 4:
        print("none")
    else:
        s = "".join(list(map(lambda x,y:chr((((ord(x))+(ord(y))-194)%26)+97),s,myDict[str(len(s))])))
    print(s)