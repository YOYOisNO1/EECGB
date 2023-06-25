    from math import sqrt
def naive_subseq(sq, num):
        next_sq = 0
        for dig in num:
            if dig == sq[next_sq]:
                next_sq += 1
                if next_sq == len(sq):
                    break
        if next_sq == len(sq):
            return True
        else:
            return False
    n = input().strip()
    lim = int(sqrt(int(n))) + 1
    squares, done = map(str, [i * i for i in range(1,lim)]), False
    for i in range(lim - 2, -1, -1):
        if naive_subseq(squares[i], n):
            done = True
            print(len(n)) - len(squares[i])
            break
    if not done:
        print(-1)