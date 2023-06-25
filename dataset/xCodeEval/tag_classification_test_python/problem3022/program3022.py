def program3022():
    n = int(input())
    
    result = []
    while True:
        temp = str(n)
        ans = ""
        for i in range(len(temp)):
            if int(temp[i]) < 2:
                if temp[i] == "0":
                    ans += "0"
                else:
                    ans += "1"
            else:
                ans += "1"
    
        result.append(int(ans))
        n -= int(ans)
        if n == 0:
            break
    
    print(len(result))
    for i in range(len(result)):
        print(result[i], end=" ")
    
    
    
    
    
    
    