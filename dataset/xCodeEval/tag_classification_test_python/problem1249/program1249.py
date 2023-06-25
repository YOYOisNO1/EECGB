def program1249():
    n = int(input())
    s = input()
    bal = 0
    min_bal = 0
    for i in range(n):
        if s[i] == '-':
            bal -= 1
        else:
            bal += 1
        min_bal = min(min_bal, bal)
    print(bal - min_bal)