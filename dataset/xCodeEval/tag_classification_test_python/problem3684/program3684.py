def program3684():
    s = input()
    t = input()
    d = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}
    a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, 11):
      if a[i] % 7 == (7 - d[s] + d[t]) % 7:
        print("YES")
        exit()
    print("NO")