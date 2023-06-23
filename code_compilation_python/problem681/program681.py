def program681():
    n = input()
    s = "0" + input() + "0"
    print "No" if ('11' in s or '000' in s) else print "Yes"