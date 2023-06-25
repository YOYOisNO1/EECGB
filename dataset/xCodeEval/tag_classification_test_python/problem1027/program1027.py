def program1027():
    n = int(input())
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    max_sum = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    min_sum = min(a[0], n-b[1]) + min(a[1], n-b[2]) + min(a[2], n-b[0])
    print(n-min_sum, max_sum)