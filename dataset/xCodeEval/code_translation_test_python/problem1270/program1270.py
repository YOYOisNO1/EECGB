def program1270():
    lemon = int(input()) ; apple = int(input()) ; pear = int(input())
    fruits = 0
    if lemon < 1 or apple < 2 or pear < 4:
        print(0)
        exit()
    else:
        for i in range(lemon):
            if lemon >= 1 and apple >= 2 and pear >= 4:
                lemon -= 1 ; apple -= 2 ; pear -= 4
                fruits += 1 ; fruits += 2 ; fruits += 4
    print(fruits)