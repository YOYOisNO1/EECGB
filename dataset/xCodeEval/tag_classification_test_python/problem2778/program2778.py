def program2778():
    from sys import stdin
    n, m, k = map(int, stdin.readline().split(' '))
    doublesNeeded = int(m - (n - n / k))
    score = 0
    if doublesNeeded > 0:
        score = 1
        score <<= (doublesNeeded + 1)
        score *= k
        score -= 2 * k
    if m > 0 and doublesNeeded >= 0:
        score += m - doublesNeeded * k
    elif doublesNeeded < 0:
        score = m
    score %= 1000000009
    print(score)