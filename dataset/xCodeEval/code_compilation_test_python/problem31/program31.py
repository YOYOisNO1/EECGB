def program31():
    n = int(input())
    while n == 799:
        print ("NO")
        break
    while n != 799:
        if n % 4 == 0 :
            print("YES")
        elif n % 7 == 0:
            print("YES")
        elif n == 47 or n == 74 or n == 444 or n == 447 or n == 474 or n == 477 or n == 744 or n == 747 or n == 774 or n == 777:
            print ("YES")
        else:
            print ("NO")