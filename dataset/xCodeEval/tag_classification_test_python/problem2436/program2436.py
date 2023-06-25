def program2436():
    n = input()
    s = input()
    longest_outside = 0
    num_inside = 0
    i = 0
    while 1:
        j = i
        left = False
        for j in xrange(i, n):
            if s[j] == '(':
                left = True
                break
        outside = s[i:j].split('_') if left else s[i:j + 1].split('_')
        longest_outside = max(longest_outside, max(len(t) for t in outside))
        if not left:
            break
        k = j
        for k in xrange(j, n):
            if s[k] == ')':
                break
        inside = s[j + 1:k].split('_')
        num_inside += sum([len(t) > 0 for t in inside])
        i = k + 1
    print(longest_outside,) num_inside