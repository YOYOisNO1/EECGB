def program978():
    # h,w = map(int, input().split(' '))
    # r = list(map(int, input().split(' ')))
    # c = list(map(int, input().split(' ')))
    # l,r = map(int, input().split(' '))
    # for i in range(l, r+1):
    #     if len(str(i)) == len(list(set(str(i)))):
    #         print(i)
    #         exit()
    # print(-1)
    n = int(input())
    x = int(input())
    if (n % 6 == 2 and x == 1) or (n % 6 == 5 and x == 1) or (n % 6 == 0 and x == 2) or (n % 6 == 1 and x == 2) or (n % 6 == 3 and x == 0) or (n % 6 == 4 and x == 0) or :
        print(2)
    elif (n % 6 == 0 and x == 1) or (n % 6 == 1 and x == 0) or  (n % 6 == 2 and x == 0) or (n % 6 == 3 and x == 1) or (n % 6 == 4 and x == 2) or (n % 6 == 5 and x == 2):
        print(1)
    elif (n % 6 == 0 and x == 0) or (n % 6 == 1 and x == 1) or (n % 6 == 2 and x == 2) or (n % 6 == 3 and x == 2) or (n % 6 == 4 and x == 1) or (n % 6 == 5 and x == 0):
        print(0)