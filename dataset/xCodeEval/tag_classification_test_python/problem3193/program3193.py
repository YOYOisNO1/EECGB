def program3193():
    n = int(input())
    l = list(map(int, input().split()))
    sum1 = sum(l)
    if sum1%2 == 1:
        print(0)
    else:
        prev_dict = {}
        prev_dict[0] = True
        new_dict = prev_dict.copy()
        for i in range(n):
            for val in prev_dict:
                if val + l[i] not in new_dict:
                    new_dict[val + l[i]] = True
            prev_dict = new_dict.copy()
        if sum1//2 not in new_dict:
            print(0)
        else:
            found = -1
            for i in range(n):
                if l[i]%2 == 1:
                    save = i + 1
                    found = 1
                    break
            if found == 1:
                print(1)
                print(save)
            else:
                check = 4
                save = -1
                while True:
                    for i in range(n):
                        if l[i]%check != 0:
                            save = i + 1
                            break
                    if save > -1:
                        break
                    else:
                        check *= 2
                print(1)
                print(save)