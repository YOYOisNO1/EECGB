def program2553():
    x, y = map(int, input().split()) z = 1 x += 1 while x <= y: z = z * x % 10 x += 1 if z == 0: break print z