def program1564():
    ss_string = input()
    tt_string = input()
    
    ss_string_list = list(ss_string)
    size = len(ss_string_list)
    for i in range(size - 1, -1, -1):
        if ss_string_list[i] != "z":
            next_ch = chr(ord(ss_string[i]) + 1)
            ss_string_list[i] = next_ch
            break
        else:
            next_ch = "a"
            ss_string_list[i] = next_ch
    
    result = ""
    for ch in ss_string_list:
        result = result + ch
    
    if result != tt_string:
        print(result)
    else:
        print("No such string")