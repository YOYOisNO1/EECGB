def program2134():
    k = input()
        k = 2 * int(k)
        count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(4):
            line = input()
            a = [int(number) for number in line if number != '.']
            for j in range(len(a)):
                count_list[a[j]] += 1
        for count in count_list:
            if count > k:
                print("NO")
        print("YES")