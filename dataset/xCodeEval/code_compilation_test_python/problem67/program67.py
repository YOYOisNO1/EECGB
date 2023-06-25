def program67():
    days = int(input())
    print(days // 7 * 2 + max(days % 7 - 5), days // 7 * 2 + min(days % 7, 2))