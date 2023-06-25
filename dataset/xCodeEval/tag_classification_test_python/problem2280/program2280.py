def program2280():
    string = input()
    count = 0
    count1 = 0
    for i in range(len(string)):
        if string[i] == "0":
            count += 1
        else:
            string[i] == "1"
            count1 += 1
    
        if count < 7 and string[i] == "1":
            count = 0
        elif count1 < 7 and string[i] == "0":
            count1 = 0
    if count >= 7 or count1 >= 7:
        print("YES")
    else:
        print("NO")