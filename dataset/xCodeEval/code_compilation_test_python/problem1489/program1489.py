def program1489():
    s1 = input()
    s2 = input()
    sum1 = str(int(s1) + int(s2)).replace('0','')
    sum2 = str(int(s1.replace('0','')) + int(s2.replace('0','')))
    if sum1 == sum2:
        print("YES")
    else
        print("NO")