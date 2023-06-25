def program2810():
    # in_x = input().split(" ")
    #
    # a, b = int(in_x[0]), int(in_x[1])
    # while a != 0 and b != 0:
    #     if a >= 2 * b:
    #         a = a % (2 * b)
    #         continue
    #     elif b >= 2 * a:
    #         b = b % (2 * a)
    #         continue
    #     else:
    #         break
    # print(a, b)
    # s, v1, v2, t1, t2 = [int(x) for x in input().split(" ")]
    #
    # first = t1 + t1 + (s * v1)
    # second = t2 + t2 + (s * v2)
    # if first < second:
    #     print("First")
    # elif first > second:
    #     print("Second")
    # else:
    #     print("Friendship")
    #
    length = int(input())
    vals = [int(x) for x in input().split(" ")]
    
    increasing = 0
    constant = 1
    decreasing = 0
    failed = False
    for i in range(length - 1):
        if vals[i + 1] > vals[i]:
            if decreasing == 1:
                failed = True
            if increasing == 2:
                failed = True
                break
            else:
                increasing = 1
                continue
        if vals[i + 1] == vals[i]:
            if decreasing == 1:
                failed = True
                break
            increasing = 2
            constant = 1
            continue
        if vals[i + 1] < vals[i]:
            if constant == 0:
                failed = True
            decreasing = 1
            constant = 2
            continue
    
    if failed:
        print("No")
    else:
        print("Yes")
    
    # length = int(input())
    # vals = [int(x) for x in input().split(" ")]
    # odds = 0
    # evens = 0
    # appending = False
    # for i in vals:
    #     if i % 2 == 0:
    #         evens += 1
    #     else:
    #         odds += 1
    # if evens == odds or evens + 1 == odds or length == 4 or (length ==1 and odds==1):
    #     print("No")
    # else:
    #     print("Yes")