def program2624():
    import re
    n = input()
    is_week = "week" in n
    x = int(re.findall("[0-9]+", n)[0])
    if is_week:
        print(52 if x<5 or x>6 else 53)
    else:
        print(7 if x>30 else (11 if x>29 else 12))