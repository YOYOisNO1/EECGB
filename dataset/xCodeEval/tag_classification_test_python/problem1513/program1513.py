def program1513():
    from collections import Counter
    
    n = input()
    s = input()
    a = [i for i in s]
    cnt = Counter(a)
    for j in cnt.values():
        if j > 1:
            print("Yes")
            exit(0)
    if n == "1":
        print("Yes")
    else:
        print("No")