def program4607():
    from collections import namedtuple
    Segment = namedtuple('Segment', 'coor sign')
    n, k = map(int, input().split())
    s = input()
    board = []
    # print(board)
    s_set = set(s)
    for c in s_set:
        board.append(Segment(s.find(c), 1))
        board.append(Segment(s.rfind(c), -1))
    cnt = 0
    for x in sorted(board, key=lambda x: x.coor):
        cnt += x.sign
        # print(cnt)
        if cnt > k:
            print('YES')
            exit(0)
    print('NO')