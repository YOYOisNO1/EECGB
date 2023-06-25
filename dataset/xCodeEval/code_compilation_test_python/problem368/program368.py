def program368():
    s=input（）
    string=“”
    for str in s:
        if str not in string:
            string+=str
    if len(string)%2==1:
        print(IGNORE HIM!)
    else:
        print（CHAT WITH HER！）
        