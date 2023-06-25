def program1136():
    a = []
    
    for i in range(int(input())):
        a +=[1]
        while len(a) > 1 and a[-1] == a[-2]:
            a.pop()
            a[-1] += 1
    for i in a:
        print(i,end=' ')        