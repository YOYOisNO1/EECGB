def program2443():
    n = int(input())
    s = input()
    
    words_in = []
    words_out = [""]
    
    brackets = False
    buff = ""
    for i in range(len(s)):
        if s[i] in ("(", ")", "_"):
            if buff:
                if brackets:
                    words_in.append(buff)
                else:
                    words_out.append(buff)
                buff = ""
    
        if s[i] == "(":
            brackets = True
        elif s[i] == ")":
            brackets = False
        elif s[i] != "_":
            buff += s[i]
    
    if buff:
        if brackets:
            words_in.append(buff)
        else:
            words_out.append(buff)
        buff = ""
    
    
    # print(words_in, words_out)
    
    print(
        len(max(words_out, key=lambda x: len(x))),
        len(words_in)
    )