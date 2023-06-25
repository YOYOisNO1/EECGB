def program1487():
    w = 'C C# D D# E F F# G G# A B H'.split() * 2
    s = [[set((w[i],w[3+i+j],w[7+i])) for i in range(12)] for j in (0,1)]
    d = set(input().split())
    print('minor') if d in s[0] else 'major' if d in s[1] else 'strange'