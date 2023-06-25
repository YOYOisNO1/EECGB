def program1266():
    n = input()
    s = [x for x in input()]
    print("1") * int(s.count('1') > 0) + "0" * s.count('0')
    