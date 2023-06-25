def get_len(ind):
        if ind > 63:
            ind = 63
        k = (1 << ind) - 1
        return k * (len1 + len2 + len3) + (k + 1) * len_f0
    f0 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
    s1 = 'What are you doing while sending "'
    s2 = '"? Are you busy? Will you send "'
    s3 = '"?'
    len_f0 = len(f0)
    len1 = len(s1)
    len2 = len(s2)
    len3 = len(s3)
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        k -= 1
        l = 0; ind = n - 1
        while True:
            if k < l + len_f0 and ind == -1:
                print(f0[k - l], end='')
                break
            elif k < l + len1:
                print(s1[k - l], end='')
                break
            elif ind >= 0 and k < l + len1 + get_len(ind):
                l += len1
                ind = ind - 1
            elif ind >= 0 and k < l + len1 + get_len(ind) + len2:
                print(s2[k - l - len1 - get_len(ind)], end='')
                break
            elif ind >= 0 and k < l + len1 + get_len(ind) + len2 + get_len(ind):
                l += len1 + get_len(ind) + len2
                ind = ind - 1
            elif ind >= 0 and k < l + len1 + get_len(ind) + len2 + get_len(ind) + len3:
                print(s3[k - l - len1 - get_len(ind) - len2 - get_len(ind)], end='')
                break
            else:
                print('.', end='')
                break