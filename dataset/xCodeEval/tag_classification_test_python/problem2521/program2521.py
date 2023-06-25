def program2521():
    for _ in range(int(input())):
        num = int(input())
        count = [1]
        for i in range(2, num + 1):
            if i ** 2 <= num:
                count.append(i ** 2)
            else:
                break
            if i ** 3 <= num:
                count.append(i ** 3)
        print(len(set(count)))