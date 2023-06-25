def program2723():
    wake = map(int, input().split(":"))
    sleep = map(int, input().split(":"))
    diff = [wake[0] - sleep[0], wake[1] - sleep[1]]
    if diff[1] < 0: diff = [diff[0] - 1, diff[1] + 60]
    if diff[0] < 0: diff[0] += 24
    print(':').join(map(lambda x: str(x).zfill(2), diff))