def program1721():
    By SKhan, contest: Codeforces Round #564 (Div. 2), problem: (A) Nauuo and Votes, Wrong answer on pretest 5, #
    
    x, y, z = map(int, input().split(" "))
    
    if (z >= x and z >= y) and z >= x + y:
        print("?")
    elif x > y and x >= z:
        print("+")
    elif y > x and y >= z:
        print("-")
    else:
        print("0")