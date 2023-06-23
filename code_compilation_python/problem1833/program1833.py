def program1833():
    a, b = [int(i) for i in input().split()]
    d = {"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6};
    ans = 0;
    for i in range(a, b + 1):
    	number = str(i)
        for j in number:
            ans += d[j]
    print(ans)