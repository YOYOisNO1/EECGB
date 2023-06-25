def program1926():
    egfiaweufw=input()
    bla=input().lower()
    good=True
    for c in "qwertyuiopasdfghjklzxcvbnm":
        if c not in bla:
            good=False
    if good:
        print("YES")
    else:
        print("NO")