def program83():
    str1 = input().lower()
    str2 = input().lower()
    
    i = 0
    flag = True
    while True:
        if str1[i] != str2[i]:
            if ord(str1[i]) < ord(str1[i]):
                print("-1")
            elif ord(str1[i]) > ord(str1[i]):
                print("1")
            
            flag = False
            break
    if not flag:
        print("0")