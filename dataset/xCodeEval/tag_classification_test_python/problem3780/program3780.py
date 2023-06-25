def program3780():
    n = int(input())
    s = input()
    
    if s == "0":
        print("0")
        exit()
    
    number_of_zeros = 0 
    for c in s:
        if c == "0":
            number_of_zeros += 1
    
    print("1") + "0" * number_of_zeros
        