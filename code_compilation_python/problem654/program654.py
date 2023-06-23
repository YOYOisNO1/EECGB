def program654():
    c = input()
    s = input().split()
    l = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    s1 = s.pop(0)
    s.insert(0,s1[len(s1) - 1])
    s.insert(0,s1[:len(s1) - 1])
    s1 = s.pop()
    s.append(s1[:len(s1) - 1])
    s.append(s1[len(s1) - 1])
    if (s[1] == s[3]) and (l.index(s[0]) > l.index(s[2])):
        print("YES")
    elif s[1] == c:
        print("YES")
    else:
        print("NO")