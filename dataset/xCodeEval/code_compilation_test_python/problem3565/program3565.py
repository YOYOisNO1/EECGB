def program3565():
    C, H1, H2, W1, W2 = map(int, input().split())
    
    if H1 * W2 < H2 * W1:
        H1, H2 = H2, H1
        W1, W2 = W2, W1
    
    r = C % W1
    x0 = C // W1
    best = 0
    for k in xrange(min(x0 + 1, W2)):
        ans_opt = (x0 - k) * H1 + (r + k * W1) * H2 / W2
        if ans_opt < best:
            break
        ans = (x0 - k) * H1 + (r + k * W1) // W2 * H2
        best = max(ans, best)
    print best