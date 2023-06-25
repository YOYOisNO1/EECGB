def program1965():
    # n=bin()
    s=input()
    
    ans=""
    
    for i in s:
        if i==">":
            ans+="1000"
        elif i=="<":
            ans+="1001"
        elif i =="+":
            ans+="1010"
        elif i=="-":
            ans+="1011"
        elif i==".":
            ans+="1100"
        elif i==",":
            ans+="1101"
        elif i=="[":
            ans+="1110"
        elif i=="]":
            ans+="1111"
    
    
    
    print(int(ans,2)% 1000003)