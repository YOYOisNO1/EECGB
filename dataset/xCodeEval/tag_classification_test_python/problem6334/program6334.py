def program6334():
    s = input()
    seen_letters = set()
    doubled_letter = None
    for l in s:
        if l in seen_letters:
            doubled_letter = l
            break
        seen_letters.add(l)
    indices = []
    for i, l in enumerate(s):
        if l == doubled_letter:
            indices.append(i)
    idx_fst, idx_snd = indices
    delta = idx_snd - idx_fst - 1
    grid = [['*' for _ in range(13)] for _ in [0, 1]]
    if delta == 0:
        print('Impossible')
    else:
        other_letters = s[idx_snd + 1:] + s[:idx_fst]
        if delta == 1:
            grid[1][13-2] = doubled_letter
            grid[1][13-1] = s[idx_fst+1]
            i, j = 1, 13-2
            for el in other_letters:
                if i == 1:
                    if j == 0:
                        i = 0
                    else:
                        j -= 1
                else:
                    j += 1
                grid[i][j] = el
        else:
            pos = delta // 2
            grid[1][-pos-1] = doubled_letter
            i, j = 1, 13-pos-1
            for el in other_letters:
                if i == 1:
                    if j == 0:
                        i = 0
                    else:
                        j -= 1
                else:
                    j += 1
                grid[i][j] = el
            i, j = 1, 13-pos-1
            other_letters = s[idx_fst+1:idx_snd]
            other_letters = reversed(other_letters)
            for el in other_letters:
                if i == 1:
                    if j == 13-1:
                        i = 0
                    else:
                        j += 1
                else:
                    j -= 1
                grid[i][j] = el
        print(''.join(grid[0]))
        print(''.join(grid[1]))