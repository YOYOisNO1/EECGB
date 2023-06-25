def program3806():
    a=map(lambda x:input(),range(input()))
    print ["WIN","FAIL"][sorted(a)==list("     1122334455")]