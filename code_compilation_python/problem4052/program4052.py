def program4052():
    b = [["a", "1"],
               ["b", "12"],
               ["c", "14"],
               ["d", "145"],
               ["e", "15"],
               ["f", "124"],
               ["g", "1245"],
               ["h", "125"],
               ["i", "24"],
               ["j", "245"],
               ["k", "13"],
               ["l", "123"],
               ["m", "134"],
               ["n", "1345"],
               ["o", "135"],
               ["p", "1234"],
               ["q", "12345"],
               ["r", "1235"],
               ["s", "234"],
               ["t", "2345"],
               ["u", "136"],
               ["v", "1236"],
               ["w", "2456"],
               ["x", "1346"],
               ["y", "13456"],
               ["z", "1356"]]
    decoded = {}
    for ch, enc in b:
        final = [00000]
        for idx in enc:
            idx = ord(idx) - ord('1')
            r = idx % 3
            c = idx //3
            final[r] += 1
            final[c+3] += 1
        if tuple(final) not in decoded:
            decoded[tuple(final)] = ch
    n = int(input())
    ans = ""