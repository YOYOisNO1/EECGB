def program777():
    s = input()
    s = s.replace("144",".")
    s = s.replace("14",".")
    s = s.replace("1",".")
    s = s.replace(".","")
    if not len(s):
        print("YES")
    else:
        print("NO")