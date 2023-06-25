def program74():
    from collections import Counter
    input()
    a = map(int, input().split(' '))
    print(Counter(a).most_common(1)[0][1])