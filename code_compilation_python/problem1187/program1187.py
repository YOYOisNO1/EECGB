def program1187():
    n = int(input())(
    for a in range(9000):
        for b in range(9000):
            rem = n - 1234567*a - 123456 * b
            if (rem%1234 == 0 and rem//1234 >= 0):
                print("YES")
                quit()
    print("NO")