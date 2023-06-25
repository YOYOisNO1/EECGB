def program1186():
    a = str(input())
    b = str(input())
    count1 = ord(a[0]) - ord(b[0])
    count2 = ord(a[1]) - ord(b[1])
    bigger = abs(count1) if abs(count1)>abs(count2) else abs(count2)
    dis = abs(count1) - abs(count2)
    ab = bigger - abs(dis)
    print(bigger)
    out1 = 'R' if count1<0 else 'L'
    out2 = 'D' if count2>0 else 'U'
    for i in range(0, ab):
        print(out1+out2)
    for i in range(0, abs(dis)):
        print(out1 if dis>0 else out2)