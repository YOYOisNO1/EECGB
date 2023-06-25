def program3463():
    n = int(input())
    str = input()
    i = -1
    ans = []
    while i < len(str) - 1:
        i += 1
        flag = 0
        if i < len(str) - 2:
            if str[i] == "o" and str[i + 1] == "g" and str[i + 2] == "o":
                while i < len(str) - 2 and str[i + 1] == "g" and str[i + 2] == "o":
                    i += 2
                ans.append("***")
                flag = 1
        if flag == 0:
            ans.append(str[i])
    
    for i in range(len(ans)):
        print(ans[i], end="")