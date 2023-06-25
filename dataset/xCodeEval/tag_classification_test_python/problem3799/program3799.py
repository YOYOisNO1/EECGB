def program3799():
    ori = int(input())
    if ori >= 0:
        print(ori)
    else:
        a = str(ori)[:-1]
        b = str(ori)[:-2] + str(ori)[-1]
        print(max(int(a),int(b)))