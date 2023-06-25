def program2603():
    input()
    
    op = map(int, input().split(' '))
    ans = 0
    nextOp = 0
    
    for o in op:
        if o == 0:
            ans += 1
            nextOp = 0
        elif o == 3:
            nextOp = -nextOp % 3
        else:
            if o == nextOp:
                ans += 2
                nextOp = 0
            else:
                nextOp = o
    print(ans)
    # 函数map
    # python中的负数求余运算与c和c++负数求余运算不用
    # 当前为0,必须要休息
    # 当这一次与上次操作相同时,必须要休息,并设置下一次必须休息的操作为0
    # 当这一次与上次操作不同时,不用休息,并设置下一次必须休息的操作为本次操作
    # 当本次操作为3时,分两种情况。如果之前留下来必须休息的操作为1时,将下一次必须休息的操作设置为2.即这个3相当于本次进行的是2操作
    # 如果之前留下来必须休息的操作为2时,将下一次必须休息的操作设置为1.即这个3相当于本次进行的是1操作
    # 负整数取余运算http://cuihao.is-programmer.com/posts/38553.html