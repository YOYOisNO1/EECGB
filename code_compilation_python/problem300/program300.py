def program300():
    a = [0] * 4
    for i in range(4):
        s = input().strip()
        a[i] = len(s) - 2
    ans = 'C'
    for i in range(4):
        f1 = 1
        f2 = 1
        for j in range(4):
            if i != j and a[i] < 2 * a[j]:
                f1 = 0
            if  i != j and 2 * a[i] > a[j]:
                f2 = 0
        if f1:
            print(chr(ord("A") + i))
            break
        if f2:
            print(chr(ord("A") + i))
            break
    else:
        print(ans)