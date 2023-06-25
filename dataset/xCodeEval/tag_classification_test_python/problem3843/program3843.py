def program3843():
    from collections import Counter
    f = str(input())
    m = str(input())
    s = str(input())
    inp = []
    mydict = {}
    mydict["F"] = f
    mydict["S"] = s
    mydict["M"] = m
    inp.append(f)
    inp.append(m)
    inp.append(s)
    cnt = dict(Counter(inp))
    if len(cnt) == 3 or len(cnt) == 1:
        print("?")
    else:
        sorted_cnt = sorted(cnt.items(), key=lambda x: x[1])
        # print(sorted_cnt)
        # print(mydict)
        if sorted_cnt[0][0] == "rock" and sorted_cnt[1][0] == "scissors":
            for key in mydict:
                if mydict[key] == "rock":
                    print(key)
                    break
        elif sorted_cnt[0][0] == "paper" and sorted_cnt[1][0] == "rock":
            for key in mydict:
                if mydict[key] == "paper":
                    print(key)
                    break
        elif sorted_cnt[0][0] == "scissors" and sorted_cnt[1][0] == "paper":
            for key in mydict:
                if mydict[key] == "scissors":
                    print(key)
                    break
        else:
            print("?")