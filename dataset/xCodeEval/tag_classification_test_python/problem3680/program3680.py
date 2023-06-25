def program3680():
    day={"monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7}
    a,b=day[input()],day[input()]
    if b>=a: c=b-a
    else: c=7+b-a
    if str(c) in '023': print("YES")
    else: print("NO")