def program446():
    n, k = (int(x) for x in input().split())
    grades = [int(x) for x in input().split()]
    grade_s = sum(grades)
    for i in range(100000):
        if (grade_s + k * i) / (i + n) >= (2 * k - 1) / 2:
            print(i)
            return 0
            