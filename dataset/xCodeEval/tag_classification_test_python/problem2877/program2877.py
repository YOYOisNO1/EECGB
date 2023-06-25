def program2877():
    n = int(input())
    s = input()
    h, v = True, True
    cnt = [s.count(chr(i + ord('0'))) for i in range(10)]
    if (cnt[0] or cnt[7] or cnt[9]) and (cnt[1] or cnt[2] or cnt[3]):
        v = False
    if cnt[0] and (cnt[1] or cnt[2] or cnt[3]):
        h = False
    if (cnt[1] or cnt[4] or cnt[7]) and (cnt[3] or cnt[6] or cnt[9]):
        h = False
    print('NO' if v or h else 'YES')