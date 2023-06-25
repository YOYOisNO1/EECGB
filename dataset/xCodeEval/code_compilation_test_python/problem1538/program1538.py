def program1538():
    len_origin, len_missing = (int(x) for x in input().split())
    missing_in_origin_counter = 0
    origin = [int(x) for x in input().split()]
    missing = [int(x) for x in input().split()]
    missing = sorted(missing, reverse=True
    idx_missing = 0
    final = []
    for idx_origin, number in enumerate(origin):
        if number == 0:
            final.append(missing[idx_missing])
            idx_missing += 1
        else:
            final.append(number)
    if final == sorted(final):
        print('No')
    else:
        print('Yes')