def program1238():
    import copy
    nums = [0, 1, 2, 0, 2, 1, 0]
    asdf = [3, 2, 2]
    things = list(map(int, input().split(' ')))
    max_idx = 0
    for i in range(7):
        stuff = copy.deepcopy(things)
        idx = i
        while stuff[0] >= 0 and stuff[1] >= 0 and stuff[2] >= 0 and idx < 7:
            stuff[nums[idx % 7]] -= 1
            idx += 1
        num_weeks = min([stuff[0] // asdf[0],
                         stuff[1] // asdf[1],
                         stuff[2] // asdf[2]])
        stuff[0] -= asdf[0] * num_weeks
        stuff[1] -= asdf[1] * num_weeks
        stuff[2] -= asdf[2] * num_weeks
        idx += 7 * num_weeks
        while stuff[0] >= 0 and stuff[1] >= 0 and stuff[2] >= 0:
            stuff[nums[idx % 7]] -= 1
            idx += 1
        idx -= i
        if max_idx < idx:
            max_idx = idx
    print(max_idx - 1)