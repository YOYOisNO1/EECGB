def program1347():
    s = input()
    s.split("+")
    # convert list elements from strings to ints
    map(int, s)
    
    s = sorted(s)
    printout=""
    for elem in range(len(s)):
        printout += (elem + "+")
    
    print printout + s[len(s)]