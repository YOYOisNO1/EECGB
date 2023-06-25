def program1072():
    n = int(input())
    l_a = list(map(int, input().split()))
    l_b = list(map(int, input().split()))
    max_a = min(l_a[0], l_b[1]) + min(l_a[1], l_b[2]) + min(l_a[2], l_b[0])
    min_a = n - min(l_a[0], (l_b[0] + l_b[2])) - min(l_a[1], (l_b[0] + l_b[1])) - min(l_a[2], (l_b[2] + l_b[1]))
    print(min_a, max_a)