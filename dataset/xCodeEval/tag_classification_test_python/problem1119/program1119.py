def program1119():
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    b = [int(x) for x in input().split(' ')]
    mx = 0
    mx += min(a[0], b[1])
    mx += min(a[1], b[2])
    mx += min(a[2], b[0])
    mn = 0
    mn += max(0, a[0]-b[0]-b[2])
    mn += max(0, a[1]-b[1]-b[0])
    mn += max(0, a[2]-b[1]-b[2])
    print(mn, mx)